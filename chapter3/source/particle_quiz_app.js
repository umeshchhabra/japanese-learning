'use strict';

const KEY = 'genki-ch3-particle-quiz-100-v2';
const $ = selector => document.querySelector(selector);
const CORE = ['を', 'に', 'で', 'へ'];
const escapeHtml = value => String(value).replace(/[&<>"']/g, char => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
})[char]);

function emptyState() {
  return QUESTIONS.map(() => ({choice: null, checked: false}));
}

function readState() {
  try {
    const saved = JSON.parse(localStorage.getItem(KEY) || 'null');
    if (Array.isArray(saved) && saved.length === QUESTIONS.length) {
      return saved.map((value, index) => {
        const choice = Number.isInteger(value?.choice) && value.choice >= 0
          && value.choice < QUESTIONS[index].choices.length ? value.choice : null;
        return {choice, checked: Boolean(value?.checked && choice !== null)};
      });
    }
  } catch (error) {}
  return emptyState();
}

let state = readState();
let current = 0;

function save() {
  try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (error) {}
}

function progress() {
  const done = state.filter(answer => answer.checked).length;
  $('#answered').textContent = `${done} answered`;
  $('#fill').style.width = `${done}%`;
  $('.track').setAttribute('aria-valuenow', done);
}

function helpMarkup(question) {
  return question.glossary.map(([word, kind, meaning]) =>
    `<li><span lang="ja">${escapeHtml(word)}</span> <small>${escapeHtml(kind)}</small> — ${escapeHtml(meaning)}</li>`
  ).join('');
}

function render() {
  const question = QUESTIONS[current];
  const answer = state[current];
  $('#counter').textContent = `Question ${current + 1} of ${QUESTIONS.length}`;
  $('#qnumber').textContent = `${String(current + 1).padStart(2, '0')} / 100`;
  $('#topic').textContent = 'Mixed particles · Lessons 1–3';
  $('#prompt').textContent = question.prompt;
  progress();

  $('#choices').innerHTML = '<legend class="small">Choose one answer.</legend>'
    + question.choices.map((choice, index) => {
      let style = 'choice';
      if (answer.checked && question.answers.includes(index)) style += ' correct';
      if (answer.checked && answer.choice === index && !question.answers.includes(index)) style += ' wrong';
      return `<label class="${style}"><input type="radio" name="answer" value="${index}" ${answer.choice === index ? 'checked' : ''}><span class="japanese" lang="ja">${escapeHtml(choice)}</span></label>`;
    }).join('');

  // Word help resets to its collapsed state for each new question.
  $('#help').open = false;
  $('#romaji').textContent = question.romaji;
  $('#glossary').innerHTML = helpMarkup(question);
  $('#previous').disabled = current === 0;
  $('#check').hidden = answer.checked;
  $('#next').hidden = !answer.checked;
  $('#next').textContent = current === QUESTIONS.length - 1 ? 'See my results' : 'Next question';

  const feedback = $('#feedback');
  if (answer.checked) {
    const correct = question.answers.includes(answer.choice);
    const accepted = question.answers.map(index => question.choices[index]).join(' / ');
    feedback.hidden = false;
    feedback.className = `feedback${correct ? '' : ' bad'}`;
    feedback.innerHTML = `<strong>${correct ? 'Correct.' : 'Take another look.'}</strong>${correct ? '' : `<span>Accepted: <span class="japanese" lang="ja">${escapeHtml(accepted)}</span>.</span><br>`}<span>${escapeHtml(question.why)}</span>`;
  } else {
    feedback.hidden = true;
  }
}

function finish() {
  const correct = state.reduce((total, answer, index) => total +
    (answer.checked && QUESTIONS[index].answers.includes(answer.choice) ? 1 : 0), 0);
  const groups = [
    ['を · objects', question => question.category === 'を'],
    ['に · time/destination', question => question.category === 'に'],
    ['で · action place', question => question.category === 'で'],
    ['へ · direction', question => question.category === 'へ'],
    ['Chapters 1–2 particles', question => !CORE.includes(question.category)]
  ];
  const breakdown = groups.map(([label, matches]) => {
    const indexes = QUESTIONS.map((question, index) => matches(question) ? index : -1)
      .filter(index => index >= 0);
    const score = indexes.filter(index => QUESTIONS[index].answers.includes(state[index].choice)).length;
    return `<div class="metric"><strong>${score} / ${indexes.length}</strong><span>${escapeHtml(label)}</span></div>`;
  }).join('');

  const missed = QUESTIONS.map((question, index) => ({question, index}))
    .filter(({question, index}) => !question.answers.includes(state[index].choice));
  const review = missed.length ? `<article class="card"><h2>Review ${missed.length} missed ${missed.length === 1 ? 'answer' : 'answers'}</h2><p class="small">Read the explanations, then try these patterns again.</p>${missed.map(({question, index}) => {
    const accepted = question.answers.map(answerIndex => question.choices[answerIndex]).join(' / ');
    return `<div class="miss"><h3>${String(index + 1).padStart(2, '0')}. ${escapeHtml(question.prompt)}</h3><p class="answerline wrongtext">Your answer: <span class="japanese" lang="ja">${escapeHtml(question.choices[state[index].choice])}</span></p><p class="answerline righttext">Accepted: <span class="japanese" lang="ja">${escapeHtml(accepted)}</span></p><p class="small">${escapeHtml(question.why)}</p><details class="help"><summary>Romaji and English word meanings</summary><p><strong>Romaji:</strong> ${escapeHtml(question.romaji)}</p><ul>${helpMarkup(question)}</ul></details></div>`;
  }).join('')}</article>` : '';

  $('#quiz').hidden = true;
  $('#results').innerHTML = `<article class="card"><div class="eyebrow">Finished</div><h2>Your result</h2><div class="score">${correct} / 100</div><p>${correct === 100 ? 'Excellent work.' : correct >= 80 ? 'Strong work. Review the missed items below.' : 'Review the explanations, then repeat the quiz to strengthen each particle pattern.'}</p><div class="breakdown">${breakdown}</div><button id="restart" class="primary">Restart all 100</button></article>${review}`;
  $('#results').hidden = false;
  $('#restart').addEventListener('click', () => {
    if (!confirm('Clear your answers and start the quiz again?')) return;
    state = emptyState();
    current = 0;
    save();
    $('#results').hidden = true;
    $('#quiz').hidden = false;
    render();
    window.scrollTo(0, 0);
  });
  window.scrollTo(0, 0);
}

$('#choices').addEventListener('change', event => {
  if (event.target.name !== 'answer') return;
  state[current] = {choice: Number(event.target.value), checked: false};
  save();
  $('#feedback').hidden = true;
  $('#check').hidden = false;
  $('#next').hidden = true;
  document.querySelectorAll('.choice').forEach(label => label.classList.remove('correct', 'wrong'));
  progress();
});

$('#check').addEventListener('click', () => {
  if (state[current].choice === null) {
    $('#feedback').hidden = false;
    $('#feedback').className = 'feedback bad';
    $('#feedback').innerHTML = '<strong>Choose an answer first.</strong>';
    $('#feedback').focus();
    return;
  }
  state[current].checked = true;
  save();
  render();
  $('#feedback').focus();
});

$('#previous').addEventListener('click', () => {
  if (current === 0) return;
  current--;
  render();
  window.scrollTo(0, 0);
});

$('#next').addEventListener('click', () => {
  if (current === QUESTIONS.length - 1) finish();
  else {
    current++;
    render();
    window.scrollTo(0, 0);
  }
});

render();
