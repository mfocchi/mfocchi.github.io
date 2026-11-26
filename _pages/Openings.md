---
title: "Openings"
permalink: /Openings/
layout: single
author_profile: true
---

<style>
  .openings { --op-accent: #1f5f8b; --op-line: rgba(127,127,127,.28); --op-soft: rgba(31,95,139,.06); }
  .openings h2 { margin-top: 2.2em; }
  .openings .lead { font-size: 1.08em; max-width: 68ch; }
  .openings .qualities { list-style: none; margin: 1.2em 0 0; padding: 0; }
  .openings .qualities li { border-left: 3px solid var(--op-accent); padding: .2em 0 .2em 1.1em; margin: 0 0 1.4em; max-width: 68ch; }
  .openings .qualities strong { display: block; font-size: 1.05em; margin-bottom: .25em; }
  .openings .notice { background: var(--op-soft); border: 1px solid var(--op-line); border-radius: 6px; padding: 1em 1.2em; max-width: 68ch; }
  .openings form { max-width: 640px; margin-top: 1.2em; }
  .openings .field { margin-bottom: 1.1em; }
  .openings .field > label, .openings fieldset legend { font-weight: 600; display: block; margin-bottom: .3em; }
  .openings .hint { font-size: .85em; opacity: .75; margin: .25em 0 0; }
  .openings fieldset { border: 1px solid var(--op-line); border-radius: 6px; padding: .8em 1em; margin: 0 0 1.1em; }
  .openings fieldset label { display: block; font-weight: normal; margin: .3em 0; }
  .openings .consent label { font-weight: normal; font-size: .9em; }
  .openings .hp { position: absolute; left: -9999px; }
  .openings button[type=submit] { background: var(--op-accent); color: #fff; border: 0; border-radius: 4px; padding: .7em 1.6em; font-size: 1em; cursor: pointer; }
  .openings button[type=submit]:disabled { opacity: .6; cursor: progress; }
  .openings button:focus-visible, .openings input:focus-visible, .openings textarea:focus-visible { outline: 3px solid var(--op-accent); outline-offset: 2px; }
  .openings #op-status { margin-top: 1em; font-weight: 600; }
  .openings #op-status.error { color: #b3261e; }
  .openings #op-status.ok { color: #1e7a3c; }
  .openings #own-source[hidden] { display: none; }
</style>

<div class="openings">

<p class="lead">I'm always glad to hear from students who want to build robots that leave the lab: robots that walk, jump, climb and fly in the real world. Below is who I'm looking for, what's currently available, and how to get in touch.</p>

<h2 id="ideal-candidate">Who I'm looking for</h2>

<p>To work under my supervision, whether for a thesis, an internship or a research stay, I look for three qualities together.</p>

<ul class="qualities">
  <li>
    <strong>A genuine passion for robotics</strong>
    You don't just like robots: you think about them on the train, you've built something on your own, you lose track of time tuning a controller. Passion is what keeps a project alive when the hardware breaks for the tenth time.
  </li>
  <li>
    <strong>Solid engineering foundations</strong>
    A strong expertise of STEM fundamentals (physics, mathematics, dynamics, control, optimization) and the coding skills to turn equations into software that runs on a real robot, typically in Python, C++ and ROS.
  </li>
  <li>
    <strong>Brilliance and initiative</strong>
    Passion and skills are the starting point, not the finish line. I'm looking for people who, given point A, find their own way from B to Z and come back with ideas I hadn't thought of: students who propose, try, fail fast and try again without waiting to be told.
  </li>
</ul>


<h2 id="current-openings">Current openings</h2>

<div class="notice">
  <p style="margin:0">There are currently <strong>no funded positions</strong> in my group (PhD scholarships, research grants or paid internships). When new calls open, they will be announced on this page and on the University of Trento website.</p>
</div>

<h2 id="apply">Apply anyway</h2>

<p>You can still apply for a thesis, an internship or a research stay supported by your own funding (for example your home university, Erasmus+, Marie Skłodowska-Curie, CSC or a national fellowship). Send your CV below: every application is read, and you will receive an answer by email.</p>

<form id="op-form" novalidate>
  <div class="field">
    <label for="op-name">Full name</label>
    <input id="op-name" name="name" type="text" required maxlength="120" autocomplete="name">
  </div>

  <div class="field">
    <label for="op-email">Email</label>
    <input id="op-email" name="email" type="email" required maxlength="200" autocomplete="email">
  </div>

  <div class="field">
    <label for="op-university">University (current or most recent)</label>
    <input id="op-university" name="university" type="text" required maxlength="200">
  </div>

  <div class="field">
    <label for="op-degree">Degree and level</label>
    <input id="op-degree" name="degree" type="text" required maxlength="200" placeholder="e.g. MSc in Mechatronics, 2nd year">
  </div>
  <fieldset>
    <legend>Funding</legend>
    <label><input type="radio" name="funding" value="own" required> I have my own funding (scholarship, grant or programme)</label>
    <label><input type="radio" name="funding" value="needs"> I would need a scholarship or funding from your group</label>

    <div id="own-source" class="field" hidden style="margin:.6em 0 0">
      <label for="op-source" style="font-weight:600">Funding source</label>
      <input id="op-source" name="funding_source" type="text" maxlength="200" placeholder="e.g. Erasmus+ traineeship, CSC scholarship">
    </div>
  </fieldset>

  <div class="field">
    <label for="op-interests">What would you like to work on? <span style="font-weight:normal">(optional)</span></label>
    <textarea id="op-interests" name="interests" rows="4" maxlength="2000"></textarea>
  </div>

  <div class="field">
    <label for="op-cv">CV (PDF, max 5 MB)</label>
    <input id="op-cv" name="cv" type="file" accept="application/pdf,.pdf" required>
    <p class="hint">Please include your transcript of records or grade average, and links to code or videos of projects you built.</p>
  </div>

  <div class="hp" aria-hidden="true">
    <label for="op-website">Leave this field empty</label>
    <input id="op-website" name="website" type="text" tabindex="-1" autocomplete="off">
  </div>
  <div class="field consent">
    <label><input id="op-consent" type="checkbox" required> I agree that my CV and the data in this form are stored for up to 3 months. I can ask for deletion at any time by writing to michele.focchi@unitn.it.</label>
  </div>


  <button type="submit" id="op-submit">Send application</button>
  <p id="op-status" role="status" aria-live="polite"></p>
</form>

</div>

<script>
(function () {
  // Paste the URL of your deployed Google Apps Script web app here (see SETUP.md).
  var ENDPOINT = 'PASTE_YOUR_APPS_SCRIPT_WEB_APP_URL_HERE';
  var MAX_MB = 5;

  var form = document.getElementById('op-form');
  var statusEl = document.getElementById('op-status');
  var submitBtn = document.getElementById('op-submit');
  var ownBox = document.getElementById('own-source');

  form.querySelectorAll('input[name=funding]').forEach(function (r) {
    r.addEventListener('change', function () { ownBox.hidden = form.funding.value !== 'own'; });
  });

  function setStatus(msg, kind) { statusEl.textContent = msg; statusEl.className = kind || ''; }

  function readAsBase64(file) {
    return new Promise(function (resolve, reject) {
      var r = new FileReader();
      r.onload = function () { resolve(String(r.result).split(',')[1]); };
      r.onerror = function () { reject(new Error('read')); };
      r.readAsDataURL(file);
    });
  }

  form.addEventListener('submit', async function (ev) {
    ev.preventDefault();
    var f = form.elements;
    var file = f.cv.files[0];

    if (!f.name.value.trim() || !f.university.value.trim() || !f.degree.value.trim()) return setStatus('Fill in your name, university and degree.', 'error');
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.email.value.trim())) return setStatus('Enter a valid email address.', 'error');
    if (!form.funding.value) return setStatus('Choose a funding option.', 'error');
    if (!file) return setStatus('Attach your CV as a PDF.', 'error');
    if (file.type !== 'application/pdf' && !/\.pdf$/i.test(file.name)) return setStatus('Your CV must be a PDF file.', 'error');
    if (file.size > MAX_MB * 1024 * 1024) return setStatus('Your CV is larger than ' + MAX_MB + ' MB. Compress it and try again.', 'error');
    if (!document.getElementById('op-consent').checked) return setStatus('Tick the consent box to send your application.', 'error');
    
    submitBtn.disabled = true;
    setStatus('Sending application…');
    try {
      var payload = {
        name: f.name.value.trim(),
        email: f.email.value.trim(),
        university: f.university.value.trim(),
        degree: f.degree.value.trim(),
        funding: form.funding.value,
        funding_source: f.funding_source.value.trim(),
        interests: f.interests.value.trim(),
        website: f.website.value,
        consent: true,
        fileName: file.name,
        fileBase64: await readAsBase64(file)
      };
      var res = await fetch(https://script.google.com/macros/s/AKfycbwtb_6iLN6yZskk0Qq3k70cA7REhgBLUFoRAavzEf2VrfLPMYDrrpTLvLR4Tl8Lfua5/exec, {
        method: 'POST',
        headers: { 'Content-Type': 'text/plain;charset=utf-8' }, // avoids a CORS preflight
        body: JSON.stringify(payload)
      });
      var out = await res.json();
      if (!out.ok) throw new Error(out.error || 'unknown');
      form.reset(); ownBox.hidden = true;
      setStatus('Application sent. Thank you, you will receive an answer by email.', 'ok');
    } catch (err) {
      setStatus('Your application could not be sent (' + err.message + '). Try again, or email your CV to michele.focchi@unitn.it.', 'error');
    } finally {
      submitBtn.disabled = false;
    }
  });
})();
</script>
