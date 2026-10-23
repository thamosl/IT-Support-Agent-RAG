const state = {
  activities: [],
  trace: [],
  questionCount: 0,
  activeFilter: "all",
  searchQuery: "",
  lastEvaluation: null
};

const kbSources = [
  ["IT Support Handbook", "Markdown", "2,184", "2m ago"],
  ["Password & MFA Policy", "Policy", "1,026", "12m ago"],
  ["VPN Troubleshooting Guide", "Guide", "842", "18m ago"],
  ["Laptop Setup Standard", "Standard", "1,417", "1h ago"],
  ["Software Access Requests", "Policy", "1,032", "2h ago"],
  ["Security Incident Playbook", "Playbook", "1,920", "3h ago"]
];

function getVerdictClass(verdict, score) {
  const v = (verdict || "").toUpperCase();
  if (v.includes("PASS") || score >= 0.70) return "pass";
  if (v.includes("WARN") || score >= 0.40) return "warning";
  return "fail";
}

function getFillClass(score) {
  if (score >= 0.70) return "fill-pass";
  if (score >= 0.40) return "fill-warning";
  return "fill-fail";
}

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

function renderEvaluation(evaluation) {
  state.lastEvaluation = evaluation;
  if (!evaluation || typeof evaluation !== "object" || Object.keys(evaluation).length === 0) {
    document.getElementById("evalEmptyState").style.display = "block";
    document.getElementById("evalActiveState").style.display = "none";
    const badge = document.getElementById("evalVerdictBadge");
    badge.className = "eval-pill eval-idle";
    badge.textContent = "Awaiting Eval";
    return;
  }

  document.getElementById("evalEmptyState").style.display = "none";
  document.getElementById("evalActiveState").style.display = "block";

  const overallScoreNum = parseFloat(evaluation.overall_score || 0);
  const overallPct = Math.round(overallScoreNum * 100);
  const verdict = evaluation.verdict || (overallScoreNum >= 0.7 ? "PASS" : "WARNING");
  const verdictCls = getVerdictClass(verdict, overallScoreNum);

  // Verdict Pill
  const badge = document.getElementById("evalVerdictBadge");
  badge.className = `eval-pill eval-${verdictCls}`;
  badge.textContent = `${verdict} · ${overallPct}%`;

  // Score Dial & SVG Circle
  document.getElementById("overallScoreText").textContent = `${overallPct}%`;
  const circle = document.getElementById("overallScoreCircle");
  circle.className = `circle ${verdictCls}`;
  circle.setAttribute("stroke-dasharray", `${overallPct}, 100`);

  // Verdict title & Critique
  document.getElementById("evalVerdictTitle").textContent = `${verdict} (${overallPct}%)`;
  document.getElementById("evalCritiqueText").textContent = evaluation.critique || "RAG quality evaluated by LLM Judge.";

  // Context Relevance
  const cr = parseFloat(evaluation.context_relevance || 0);
  const crPct = Math.round(cr * 100);
  document.getElementById("contextRelValue").textContent = `${crPct}%`;
  const crBar = document.getElementById("contextRelBar");
  crBar.style.width = `${crPct}%`;
  crBar.className = `metric-bar-fill ${getFillClass(cr)}`;
  document.getElementById("contextRelReasoning").textContent = evaluation.context_relevance_reasoning || "";

  // Groundedness
  const gr = parseFloat(evaluation.groundedness || 0);
  const grPct = Math.round(gr * 100);
  document.getElementById("groundednessValue").textContent = `${grPct}%`;
  const grBar = document.getElementById("groundednessBar");
  grBar.style.width = `${grPct}%`;
  grBar.className = `metric-bar-fill ${getFillClass(gr)}`;
  document.getElementById("groundednessReasoning").textContent = evaluation.groundedness_reasoning || "";

  // Answer Relevancy
  const ar = parseFloat(evaluation.answer_relevance || 0);
  const arPct = Math.round(ar * 100);
  document.getElementById("answerRelValue").textContent = `${arPct}%`;
  const arBar = document.getElementById("answerRelBar");
  arBar.style.width = `${arPct}%`;
  arBar.className = `metric-bar-fill ${getFillClass(ar)}`;
  document.getElementById("answerRelReasoning").textContent = evaluation.answer_relevance_reasoning || "";

  // Chunks Breakdown
  const chunks = Array.isArray(evaluation.chunk_evaluations) ? evaluation.chunk_evaluations : [];
  document.getElementById("chunkCount").textContent = chunks.length;
  const chunkList = document.getElementById("chunkEvalList");
  if (chunks.length === 0) {
    chunkList.innerHTML = `<div class="chunk-eval-item" style="color:#8b95a5">No individual chunks evaluated for this response.</div>`;
  } else {
    chunkList.innerHTML = chunks.map(c => {
      const cScore = parseFloat(c.score || 0);
      const cPct = Math.round(cScore * 100);
      const cCls = getVerdictClass(c.is_relevant ? "PASS" : "WARNING", cScore);
      return `
        <div class="chunk-eval-item">
          <div class="chunk-item-top">
            <span class="chunk-source" title="${escapeHtml(c.source)}">#${c.chunk_index} · ${escapeHtml(c.source)}</span>
            <span class="chunk-score-pill eval-pill eval-${cCls}">${cPct}% Relevant</span>
          </div>
          ${c.snippet ? `<div class="chunk-snippet">"${escapeHtml(c.snippet)}"</div>` : ""}
          <div class="chunk-reason">${escapeHtml(c.reasoning || "")}</div>
        </div>
      `;
    }).join("");
  }
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

  const evaluation = result.evaluation || {};
  let evalPillHtml = "";
  if (evaluation && evaluation.overall_score !== undefined) {
    const scorePct = Math.round(parseFloat(evaluation.overall_score || 0) * 100);
    const grPct = Math.round(parseFloat(evaluation.groundedness || 0) * 100);
    const crPct = Math.round(parseFloat(evaluation.context_relevance || 0) * 100);
    const arPct = Math.round(parseFloat(evaluation.answer_relevance || 0) * 100);
    const verdict = evaluation.verdict || "PASS";
    const vCls = getVerdictClass(verdict, parseFloat(evaluation.overall_score || 0));

    evalPillHtml = `
      <div class="msg-eval-pill" title="Click to view full evaluation in Inspector" onclick="focusEvalCard()">
        <span class="eval-mini-dot ${vCls}"></span>
        <span>⚖️ LLM Judge: <b>${scorePct}%</b> (${verdict}) · Grounded <b>${grPct}%</b> · Relevance <b>${arPct}%</b></span>
      </div>
    `;
  }

  messages.insertAdjacentHTML("beforeend", `
    <div class="assistant-message">
      <div class="bot-avatar">✦</div>
      <div class="assistant-content">
        <div class="message-meta"><b>Support Copilot</b><span>Just now</span></div>
        <div class="answer-card">
          <p>${escapeHtml(result.answer)}</p>
          <div style="display:flex; flex-wrap:wrap; gap:8px; align-items:center; margin-top:8px;">
            <span class="source-tag">● ${tag}</span>
            ${evalPillHtml}
          </div>
        </div>
      </div>
    </div>`);
  messages.scrollTop = messages.scrollHeight;
}

function focusEvalCard() {
  const card = document.getElementById("evalCard");
  if (card) {
    card.scrollIntoView({ behavior: "smooth", block: "nearest" });
    card.style.transition = "box-shadow 0.3s";
    card.style.boxShadow = "0 0 0 3px rgba(99, 91, 255, 0.4)";
    setTimeout(() => { card.style.boxShadow = ""; }, 1200);
  }
}

function escapeHtml(str) {
  return String(str || "").replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]));
}

async function runAgent(question) {
  document.getElementById("traceStatus").textContent = "Running";
  document.getElementById("traceList").innerHTML = `<div class="trace-item">Routing query and initiating RAG pipeline…</div>`;
  
  // Show evaluating state on eval card
  const badge = document.getElementById("evalVerdictBadge");
  badge.className = "eval-pill eval-idle";
  badge.textContent = "Judging…";

  const response = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  });
  const responseText = await response.text();
  let payload;
  try {
    payload = responseText ? JSON.parse(responseText) : {};
  } catch {
    payload = null;
  }
  if (!response.ok) {
    const message = typeof payload?.detail === "string" ? payload.detail :
      typeof payload?.error?.message === "string" ? payload.error.message :
        typeof payload?.message === "string" ? payload.message :
          response.status >= 500
            ? `The service is temporarily unavailable (${response.status}). Please try again in a moment.`
            : `Request failed (${response.status}). Please try again.`;
    throw new Error(message);
  }
  if (!payload || typeof payload !== "object" || Array.isArray(payload)) {
    throw new Error("The server returned an invalid response. Please try again.");
  }
  if (typeof payload.answer !== "string" || !payload.answer.trim()) {
    throw new Error("The assistant returned an empty answer.");
  }
  const result = {
    answer: payload.answer,
    source: payload.source_used,
    trace: Array.isArray(payload.trace) ? payload.trace : [],
    evidence: Array.isArray(payload.citations) ? payload.citations : [],
    evaluation: payload.evaluation || {}
  };

  renderTrace(result.trace);
  renderEvidence(result);
  renderEvaluation(result.evaluation);
  appendAssistant(result);

  state.questionCount++;
  document.getElementById("sessionLabel").textContent = `Session · ${state.questionCount} question${state.questionCount === 1 ? "" : "s"}`;
  
  // Refresh activity in background
  loadActivityData();
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

async function loadActivityData() {
  try {
    const [actRes, sumRes] = await Promise.all([
      fetch("/api/activity?limit=50"),
      fetch("/api/evaluations/summary")
    ]);
    if (actRes.ok) {
      const actData = await actRes.json();
      state.activities = actData.activities || [];
    }
    if (sumRes.ok) {
      const summary = await sumRes.json();
      renderSummaryCards(summary);
    }
    renderActivity();
  } catch (err) {
    console.error("Failed to load activity or summary data:", err);
  }
}

function renderSummaryCards(summary) {
  if (!summary || summary.total_evaluated === 0) {
    document.getElementById("summaryAvgScore").textContent = "—";
    document.getElementById("summaryPassRate").textContent = "Pass rate: —";
    document.getElementById("summaryAvgContext").textContent = "—";
    document.getElementById("summaryAvgGrounded").textContent = "—";
    document.getElementById("summaryAvgAnswer").textContent = "—";
    return;
  }

  const avgScore = Math.round((summary.avg_overall_score || 0) * 100);
  const avgCtx = Math.round((summary.avg_context_relevance || 0) * 100);
  const avgGrd = Math.round((summary.avg_groundedness || 0) * 100);
  const avgAns = Math.round((summary.avg_answer_relevance || 0) * 100);

  document.getElementById("summaryAvgScore").textContent = `${avgScore}%`;
  document.getElementById("summaryPassRate").textContent = `Pass rate: ${summary.pass_rate}% (${summary.total_evaluated} runs)`;
  document.getElementById("summaryAvgContext").textContent = `${avgCtx}%`;
  document.getElementById("summaryAvgGrounded").textContent = `${avgGrd}%`;
  document.getElementById("summaryAvgAnswer").textContent = `${avgAns}%`;
}

function renderActivity() {
  const el = document.getElementById("activityList");
  let list = state.activities || [];

  // Filter by Verdict
  if (state.activeFilter !== "all") {
    list = list.filter(item => {
      const evalObj = item.evaluation || {};
      const verdict = (evalObj.verdict || "").toLowerCase();
      return verdict === state.activeFilter;
    });
  }

  // Filter by Search Query
  if (state.searchQuery.trim()) {
    const q = state.searchQuery.toLowerCase();
    list = list.filter(item =>
      (item.question && item.question.toLowerCase().includes(q)) ||
      (item.source_used && item.source_used.toLowerCase().includes(q))
    );
  }

  if (!list.length) {
    el.innerHTML = `<div class="activity-card-eval" style="text-align:center; padding: 24px; color:#8e9aac">
      <b>No evaluation records found</b>
      <p style="margin-top:6px; font-size:11px;">Ask questions in the Copilot view to populate RAG evaluation activity.</p>
    </div>`;
    return;
  }

  el.innerHTML = list.map(a => {
    const ev = a.evaluation || {};
    const hasEval = ev && Object.keys(ev).length > 0 && ev.overall_score !== undefined;
    const overallScore = hasEval ? Math.round(parseFloat(ev.overall_score) * 100) : null;
    const verdict = hasEval ? (ev.verdict || "PASS") : "LOGGED";
    const vCls = hasEval ? getVerdictClass(verdict, parseFloat(ev.overall_score)) : "idle";

    const crPct = hasEval ? Math.round(parseFloat(ev.context_relevance || 0) * 100) : 0;
    const grPct = hasEval ? Math.round(parseFloat(ev.groundedness || 0) * 100) : 0;
    const arPct = hasEval ? Math.round(parseFloat(ev.answer_relevance || 0) * 100) : 0;

    const timeFormatted = a.created_at ? new Date(a.created_at).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}) : "Just now";

    return `
      <div class="activity-card-eval">
        <div class="activity-top">
          <div>
            <div class="activity-q">${escapeHtml(a.question)}</div>
            <div class="activity-meta">
              <span>● ${escapeHtml(a.source_used)}</span>
              <span>·</span>
              <span>${timeFormatted}</span>
            </div>
          </div>
          <span class="activity-verdict-badge eval-pill eval-${vCls}">
            ${verdict} ${overallScore !== null ? `· ${overallScore}%` : ""}
          </span>
        </div>

        ${hasEval ? `
          <div class="activity-metrics-row">
            <div class="act-metric">
              <div class="act-metric-title"><span>Context Relevance</span><b>${crPct}%</b></div>
              <div class="act-track"><div class="act-fill ${getFillClass(ev.context_relevance)}" style="width:${crPct}%"></div></div>
            </div>
            <div class="act-metric">
              <div class="act-metric-title"><span>Groundedness</span><b>${grPct}%</b></div>
              <div class="act-track"><div class="act-fill ${getFillClass(ev.groundedness)}" style="width:${grPct}%"></div></div>
            </div>
            <div class="act-metric">
              <div class="act-metric-title"><span>Answer Relevancy</span><b>${arPct}%</b></div>
              <div class="act-track"><div class="act-fill ${getFillClass(ev.answer_relevance)}" style="width:${arPct}%"></div></div>
            </div>
          </div>
          ${ev.critique ? `<div class="activity-critique">⚖️ <i>${escapeHtml(ev.critique)}</i></div>` : ""}
        ` : ""}
      </div>
    `;
  }).join("");
}

function showView(view) {
  document.querySelectorAll(".view").forEach(v => v.classList.remove("active-view"));
  document.getElementById(view + "View").classList.add("active-view");
  document.querySelectorAll(".nav-item").forEach(n => n.classList.toggle("active", n.dataset.view === view));
  if (view === "knowledge") renderKB();
  if (view === "activity") loadActivityData();
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
  messages.innerHTML = `<div class="welcome-message"><div class="bot-avatar">✦</div><div class="message-body"><div class="message-meta"><b>Support Copilot</b><span>Just now</span></div><p>New session started. Ask any IT support issue and see real-time LLM Judge evaluation.</p></div></div>`;
  document.getElementById("traceList").innerHTML = `<div class="trace-empty">Ask a question to see the agent workflow.</div>`;
  document.getElementById("traceStatus").textContent = "Idle";
  document.getElementById("evidenceBadge").textContent = "None";
  document.getElementById("evidenceBadge").className = "neutral-badge";
  document.getElementById("evidenceContent").textContent = "Evidence used for the current answer will appear here.";
  document.getElementById("sessionLabel").textContent = "New session · Ready";
  renderEvaluation(null);
});

document.getElementById("kbSearch").addEventListener("input", e => renderKB(e.target.value));

document.getElementById("settingsBtn").addEventListener("click", () => {
  const toast = document.getElementById("toast");
  toast.textContent = "Settings panel is ready for backend configuration.";
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 2200);
});

// Chunks toggle accordion
document.getElementById("chunkEvalToggle").addEventListener("click", () => {
  const list = document.getElementById("chunkEvalList");
  const icon = document.getElementById("chunkToggleIcon");
  list.classList.toggle("open");
  icon.classList.toggle("open");
});

// Refresh activity
document.getElementById("refreshActivityBtn").addEventListener("click", async () => {
  await loadActivityData();
  const toast = document.getElementById("toast");
  toast.textContent = "Evaluation metrics and activity refreshed.";
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 2000);
});

// Filter chips in Activity view
document.querySelectorAll(".filter-chip").forEach(chip => {
  chip.addEventListener("click", e => {
    document.querySelectorAll(".filter-chip").forEach(c => c.classList.remove("active"));
    e.target.classList.add("active");
    state.activeFilter = e.target.dataset.filter;
    renderActivity();
  });
});

// Search in Activity view
document.getElementById("activitySearch").addEventListener("input", e => {
  state.searchQuery = e.target.value;
  renderActivity();
});

// Initial boot
renderKB();
loadActivityData();
