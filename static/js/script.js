const state = {
  activities: [],
  trace: [],
  questionCount: 0
};

const kbSources = [
  ["IT Support Handbook", "Markdown", "2,184", "2m ago"],
  ["Password & MFA Policy", "Policy", "1,026", "12m ago"],
  ["VPN Troubleshooting Guide", "Guide", "842", "18m ago"],
  ["Laptop Setup Standard", "Standard", "1,417", "1h ago"],
  ["Software Access Requests", "Policy", "1,032", "2h ago"],
  ["Security Incident Playbook", "Playbook", "1,920", "3h ago"]
];

function renderTrace(items) {
  const list = document.getElementById("traceList");
  list.innerHTML = items.map(item => `<div class="trace-item done">${escapeHtml(item)}</div>`).join("");
  document.getElementById("traceStatus").textContent = "Completed";
}

function renderEvidence(result) {
  const badge = document.getElementById("evidenceBadge");
  badge.textContent = result.source === "private_kb" ? "Private KB" :
    result.source === "web_search" ? "Web search" : "No evidence";
  badge.className = result.source === "private_kb" ? "good-badge" :
    result.source === "web_search" ? "web-badge" : "neutral-badge";
  const evidence = result.evidence;
  document.getElementById("evidenceContent").innerHTML = evidence.length
    ? evidence.map(item => {
      const title = typeof item === "string" ? item : item.title || item.url || "Source";
      const description = typeof item === "string"
        ? result.source === "private_kb" ? "Private KB source" : "External search source"
        : item.type === "private_kb" ? "Private KB source" : "External web source";
      const link = typeof item === "object" && /^https?:\/\//i.test(item.url || "")
        ? `<a href="${escapeHtml(item.url)}" target="_blank" rel="noopener noreferrer">Open source</a>`
        : "";
      return `<div class="evidence-item"><b>${escapeHtml(title)}</b><span>${description}</span>${link}</div>`;
    }).join("")
    : `<div class="evidence-empty">No source citations were returned for this answer.</div>`;
}

function appendUser(text) {
  const messages = document.getElementById("messages");
  messages.insertAdjacentHTML("beforeend", `<div class="user-message"><div class="user-bubble">${escapeHtml(text)}</div></div>`);
  messages.scrollTop = messages.scrollHeight;
}

function appendAssistant(result) {
  const messages = document.getElementById("messages");
  const tag = {
    private_kb: "Private KB",
    web_search: "Web search",
    direct: "Direct answer",
    insufficient_evidence: "Insufficient evidence"
  }[result.source] || "Assistant";
  messages.insertAdjacentHTML("beforeend", `
    <div class="assistant-message">
      <div class="bot-avatar">✦</div>
      <div class="assistant-content">
        <div class="message-meta"><b>Support Copilot</b><span>Just now</span></div>
        <div class="answer-card">
          <p>${escapeHtml(result.answer)}</p>
          <span class="source-tag">● ${tag}</span>
        </div>
      </div>
    </div>`);
  messages.scrollTop = messages.scrollHeight;
}

function escapeHtml(str) {
  return String(str).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]));
}

async function runAgent(question) {
  document.getElementById("traceStatus").textContent = "Running";
  document.getElementById("traceList").innerHTML = `<div class="trace-item">Sending question to assistant…</div>`;
  const response = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  });
  const payload = await response.json();
  if (!response.ok) {
    throw new Error(payload.detail || `Request failed (${response.status})`);
  }
  if (typeof payload.answer !== "string" || !payload.answer.trim()) {
    throw new Error("The assistant returned an empty answer.");
  }
  const result = {
    answer: payload.answer,
    source: payload.source_used,
    trace: Array.isArray(payload.trace) ? payload.trace : [],
    evidence: Array.isArray(payload.citations) ? payload.citations : []
  };
  renderTrace(result.trace);
  renderEvidence(result);
  appendAssistant(result);

  state.questionCount++;
  state.activities.unshift({
    q: question,
    source: result.source,
    time: "Just now"
  });
  document.getElementById("sessionLabel").textContent = `Session · ${state.questionCount} question${state.questionCount === 1 ? "" : "s"}`;
  renderActivity();
}

function appendError(error) {
  document.getElementById("traceStatus").textContent = "Error";
  document.getElementById("traceList").innerHTML =
    `<div class="trace-empty">${escapeHtml(error.message)}</div>`;
  const messages = document.getElementById("messages");
  messages.insertAdjacentHTML("beforeend", `
    <div class="assistant-message">
      <div class="bot-avatar">!</div>
      <div class="assistant-content">
        <div class="message-meta"><b>Request failed</b><span>Just now</span></div>
        <div class="answer-card"><p>${escapeHtml(error.message)}</p></div>
      </div>
    </div>`);
  messages.scrollTop = messages.scrollHeight;
}

function renderKB(filter = "") {
  const rows = kbSources.filter(r => r[0].toLowerCase().includes(filter.toLowerCase()));
  document.getElementById("kbTable").innerHTML = rows.map(r => `
    <tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td>${r[2]}</td>
    <td><span class="status-ok">Indexed</span></td><td>${r[3]}</td></tr>`).join("");
}

function renderActivity() {
  const el = document.getElementById("activityList");
  if (!state.activities.length) {
    el.innerHTML = `<div class="activity-item"><div><b>No activity yet</b><p>Completed agent runs will appear here.</p></div><span>—</span></div>`;
    return;
  }
  el.innerHTML = state.activities.map(a => `
    <div class="activity-item"><div><b>${escapeHtml(a.q)}</b>
    <p>${a.source === "private_kb" ? "Private KB → verified answer" : "KB weak → web fallback → verified answer"}</p></div><span>${a.time}</span></div>`).join("");
}

function showView(view) {
  document.querySelectorAll(".view").forEach(v => v.classList.remove("active-view"));
  document.getElementById(view + "View").classList.add("active-view");
  document.querySelectorAll(".nav-item").forEach(n => n.classList.toggle("active", n.dataset.view === view));
  if (view === "knowledge") renderKB();
  if (view === "activity") renderActivity();
}

document.querySelectorAll(".nav-item").forEach(btn => btn.addEventListener("click", () => showView(btn.dataset.view)));

document.getElementById("chatForm").addEventListener("submit", async e => {
  e.preventDefault();
  const input = document.getElementById("questionInput");
  const sendButton = e.currentTarget.querySelector('button[type="submit"]');
  const question = input.value.trim();
  if (!question || sendButton.disabled) return;
  appendUser(question);
  input.value = "";
  input.style.height = "auto";
  sendButton.disabled = true;
  try {
    await runAgent(question);
  } catch (error) {
    appendError(error);
  } finally {
    sendButton.disabled = false;
  }
});

document.querySelectorAll(".suggestion").forEach(btn => btn.addEventListener("click", () => {
  document.getElementById("questionInput").value = btn.textContent;
  document.getElementById("questionInput").focus();
}));

document.getElementById("questionInput").addEventListener("keydown", e => {
  if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
    document.getElementById("chatForm").requestSubmit();
  }
  e.target.style.height = "auto";
  e.target.style.height = Math.min(e.target.scrollHeight, 100) + "px";
});

document.getElementById("newChatBtn").addEventListener("click", () => {
  const messages = document.getElementById("messages");
  messages.innerHTML = `<div class="welcome-message"><div class="bot-avatar">✦</div><div class="message-body"><div class="message-meta"><b>Support Copilot</b><span>Just now</span></div><p>New session started. What IT issue can I help you with?</p></div></div>`;
  document.getElementById("traceList").innerHTML = `<div class="trace-empty">Ask a question to see the agent workflow.</div>`;
  document.getElementById("traceStatus").textContent = "Idle";
  document.getElementById("evidenceBadge").textContent = "None";
  document.getElementById("evidenceBadge").className = "neutral-badge";
  document.getElementById("evidenceContent").textContent = "Evidence used for the current answer will appear here.";
  document.getElementById("sessionLabel").textContent = "New session · Ready";
});

document.getElementById("kbSearch").addEventListener("input", e => renderKB(e.target.value));

document.getElementById("settingsBtn").addEventListener("click", () => {
  const toast = document.getElementById("toast");
  toast.textContent = "Settings panel is ready for backend configuration.";
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 2200);
});

renderKB();
renderActivity();
