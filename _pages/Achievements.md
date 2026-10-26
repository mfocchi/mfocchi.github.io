---
title: "Achievements"
permalink: /Achievements/
header:
classes: wide
---

Patents, open-source software, robots I helped build, and the experiments that came out of them. Click a thumbnail to watch the video on YouTube.

<style>
.ach-tabbar { display: flex; flex-wrap: wrap; gap: .4em; margin: 1.5em 0 1em; padding-bottom: .8em; border-bottom: 1px solid rgba(128,128,128,.35); }
.ach-tabbar button { font: inherit; font-size: .8em; color: inherit; background: transparent; cursor: pointer; padding: .45em .9em; border: 1px solid rgba(128,128,128,.45); border-radius: 999px; opacity: .8; }
.ach-tabbar button:hover { opacity: 1; }
.ach-tabbar button[aria-selected="true"] { opacity: 1; font-weight: bold; background: rgba(128,128,128,.25); border-color: currentColor; }
.ach-tabbar .n { opacity: .65; margin-left: .3em; font-weight: normal; }
.ach-section h2 { margin-top: 1.6em; }
.ach-grid { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(13.5rem, 1fr)); gap: 1.4em 1.1em; }
.ach-grid li { margin: 0; }
.ach-grid a { color: inherit; text-decoration: none; display: block; }
.ach-thumb { position: relative; aspect-ratio: 16 / 9; overflow: hidden; border-radius: 6px; background: rgba(128,128,128,.2); }
.ach-thumb img { width: 100%; height: 100%; object-fit: cover; display: block; }
.ach-thumb::after { content: ""; position: absolute; left: 50%; top: 50%; width: 2.6em; height: 1.8em; transform: translate(-50%,-50%); border-radius: .45em; background: rgba(0,0,0,.65) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 10 10'%3E%3Cpath d='M3 2l5 3-5 3z' fill='white'/%3E%3C/svg%3E") center / 1em no-repeat; }
.ach-grid a:hover .ach-thumb::after, .ach-grid a:focus-visible .ach-thumb::after { background-color: #c00; }
.ach-grid a:focus-visible { outline: 2px solid currentColor; outline-offset: 3px; border-radius: 6px; }
.ach-cap { font-size: .78em; line-height: 1.4; margin-top: .45em; }
.ach-cap .y { opacity: .6; margin-left: .35em; }
.ach-cap .src { display: block; font-size: .9em; margin-top: .2em; }
.ach-cap .src a { display: inline; text-decoration: underline; }
.ach-text { border: 1px solid rgba(128,128,128,.35); border-radius: 6px; padding: .8em .9em; }
.ach-js .ach-section { display: none; }
.ach-js .ach-section.active { display: block; }
</style>

<div class="ach-tabbar" id="ach-tabbar" role="tablist" hidden><button type="button" role="tab" data-tab="all" aria-selected="false">All<span class="n">27</span></button><button type="button" role="tab" data-tab="patents" aria-selected="false">Patents<span class="n">2</span></button><button type="button" role="tab" data-tab="software" aria-selected="false">Software<span class="n">2</span></button><button type="button" role="tab" data-tab="platforms" aria-selected="false">Novel platforms<span class="n">3</span></button><button type="button" role="tab" data-tab="vehicles" aria-selected="false">Wheeled and tracked vehicles<span class="n">2</span></button><button type="button" role="tab" data-tab="legged" aria-selected="false">Legged robots<span class="n">18</span></button></div>

<section class="ach-section" id="ach-patents">
<h2>Patents</h2>
<ul class="ach-grid">
<li><div class="ach-text ach-cap">Cooperative system for aerial transport and manipulation (Sistema cooperativo per trasporto e manipolazione aerea)<span class="src"><a href="https://www.knowledge-share.eu/it/brevetti/sistema-cooperativo-per-trasporto-e-manipolazione-aerea">Patent page</a></span></div></li>
<li><div class="ach-text ach-cap">Microturbine, patent WO 2012/004738 <span class="y">2012</span><span class="src"><a href="https://worldwide.espacenet.com/searchResults?compact=false&ST=singleline&query=IT1394249">Espacenet</a></span></div></li>
</ul>
</section>

<section class="ach-section" id="ach-software">
<h2>Software</h2>
<ul class="ach-grid">
<li><a href="https://www.youtube.com/watch?v=tW5CuDmQTII"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/tW5CuDmQTII/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=tW5CuDmQTII">Locosim robotics framework</a> <span class="src"><a href="https://github.com/mfocchi/locosim">Code on GitHub</a></span></div></li>
<li><a href="https://www.youtube.com/watch?v=O6TSUHiwSlU"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/O6TSUHiwSlU/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=O6TSUHiwSlU">WoLF whole-body locomotion framework</a> <span class="src"><a href="https://github.com/graiola/wolf-setup">Code on GitHub</a></span></div></li>
</ul>
</section>

<section class="ach-section" id="ach-platforms">
<h2>Novel platforms</h2>
<ul class="ach-grid">
<li><a href="https://www.youtube.com/watch?v=FqsREaoe-28"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/FqsREaoe-28/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=FqsREaoe-28">ALPINE climbing robot</a> <span class="y">2025</span></div></li>
<li><div class="ach-text ach-cap">ALPINE real prototype <span class="y">2025</span><span class="src"><a href="https://www.dropbox.com/scl/fi/nwy5yg2yx3qe81lkw2msr/alpine.mp4?rlkey=27e0gv2bp3kf9ohx92u9ez9u5&dl=0">Watch the video</a></span></div></li>
<li><a href="https://www.youtube.com/watch?v=q9NsmhQHHFE"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/q9NsmhQHHFE/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=q9NsmhQHHFE">Microturbine</a> <span class="y">2012</span></div></li>
</ul>
</section>

<section class="ach-section" id="ach-vehicles">
<h2>Wheeled and tracked vehicles</h2>
<ul class="ach-grid">
<li><a href="https://www.youtube.com/watch?v=OfC-wzxXLpg"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/OfC-wzxXLpg/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=OfC-wzxXLpg">Shared control of wheeled vehicles for autonomous orchard exploration</a> <span class="y">2025</span></div></li>
<li><a href="https://www.youtube.com/watch?v=TyeZ0vRkI04"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/TyeZ0vRkI04/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=TyeZ0vRkI04">Slippage-aware controller for tracked vehicles</a> <span class="y">2025</span></div></li>
</ul>
</section>

<section class="ach-section" id="ach-legged">
<h2>Legged robots</h2>
<ul class="ach-grid">
<li><a href="https://www.youtube.com/watch?v=ENHvCGrnr2g"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/ENHvCGrnr2g/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=ENHvCGrnr2g">HyQ early results summary</a> <span class="y">2024</span></div></li>
<li><a href="https://www.youtube.com/watch?v=wiuedeHfSEY"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/wiuedeHfSEY/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=wiuedeHfSEY">Landing strategy for quadrupeds</a> <span class="y">2023</span></div></li>
<li><a href="https://www.youtube.com/watch?v=vJpNWnMh0wE"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/vJpNWnMh0wE/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=vJpNWnMh0wE">Aliengo walking down a 45° ramp with a rope</a> <span class="y">2023</span></div></li>
<li><a href="https://www.youtube.com/watch?v=sC-NCTl6_0A"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/sC-NCTl6_0A/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=sC-NCTl6_0A">Loco-manipulation with a tele-operated centaur robot (INAIL project)</a> <span class="y">2023</span></div></li>
<li><a href="https://www.youtube.com/watch?v=Zad20mtFJm0"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/Zad20mtFJm0/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=Zad20mtFJm0">Flywheels to control orientation during jumps</a> <span class="y">2023</span></div></li>
<li><a href="https://www.youtube.com/watch?v=r0-KIiw0eWM"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/r0-KIiw0eWM/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=r0-KIiw0eWM">HyQ crossing a relocated pallet with model predictive control</a> <span class="y">2021</span></div></li>
<li><a href="https://youtu.be/LUyq57rwovU?t=137"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/LUyq57rwovU/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://youtu.be/LUyq57rwovU?t=137">Space exploration with legged robots</a> <span class="y">2020</span></div></li>
<li><a href="https://www.youtube.com/watch?v=0BI4581DFjY"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/0BI4581DFjY/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=0BI4581DFjY">HyQ trotting on foam</a> <span class="y">2020</span></div></li>
<li><a href="https://www.youtube.com/watch?v=pLsNs1ZS_TI"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/pLsNs1ZS_TI/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=pLsNs1ZS_TI">HyQReal pulling a 3-ton airplane</a> <span class="y">2019</span></div></li>
<li><a href="https://www.youtube.com/watch?v=rxn79dPnaCI"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/rxn79dPnaCI/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=rxn79dPnaCI">Crossing pallets with neural-network foothold planning</a> <span class="y">2019</span></div></li>
<li><a href="https://www.youtube.com/watch?v=MWTmqse0ntg"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/MWTmqse0ntg/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=MWTmqse0ntg">HyQ on combined terrain (stones and ramp) with heuristic planning</a> <span class="y">2017</span></div></li>
<li><a href="https://www.youtube.com/watch?v=vD5PTUf6rLQ"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/vD5PTUf6rLQ/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=vD5PTUf6rLQ">Height reflex</a> <span class="y">2017</span></div></li>
<li><a href="https://www.youtube.com/watch?v=3zZE9YTGRjw"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/3zZE9YTGRjw/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=3zZE9YTGRjw">HyQ with online payload identification</a> <span class="y">2017</span></div></li>
<li><a href="https://www.youtube.com/watch?v=LsR3_ZgiAWs"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/LsR3_ZgiAWs/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=LsR3_ZgiAWs">HyQ stair climbing</a> <span class="y">2017</span></div></li>
<li><a href="https://www.youtube.com/watch?v=-qQp2RwQ-PQ"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/-qQp2RwQ-PQ/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=-qQp2RwQ-PQ">HyQ chimney climbing</a> <span class="y">2016</span></div></li>
<li><a href="https://www.youtube.com/watch?v=RKwWxEc-ric"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/RKwWxEc-ric/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=RKwWxEc-ric">Early work on centaur robots</a> <span class="y">2016</span></div></li>
<li><a href="https://www.youtube.com/watch?v=_9H8EIs-hMc"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/_9H8EIs-hMc/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=_9H8EIs-hMc">Step reflex</a> <span class="y">2013</span></div></li>
<li><a href="https://www.youtube.com/watch?v=e5m1SmGV_ao"><div class="ach-thumb"><img src="https://i.ytimg.com/vi/e5m1SmGV_ao/hqdefault.jpg" alt="" loading="lazy" onerror="this.remove()"></div></a><div class="ach-cap"><a href="https://www.youtube.com/watch?v=e5m1SmGV_ao">Magnetorheologically damped compliant foot</a> <span class="y">2012</span></div></li>
</ul>
</section>

<script>
(function () {
  var bar = document.getElementById('ach-tabbar');
  var secs = document.querySelectorAll('.ach-section');
  if (!bar || !secs.length) { return; }
  document.documentElement.classList.add('ach-js');
  bar.hidden = false;
  function show(key, push) {
    var known = key === 'all';
    for (var i = 0; i < secs.length; i++) { known = known || secs[i].id === 'ach-' + key; }
    if (!known) { key = 'all'; }
    for (var j = 0; j < secs.length; j++) {
      secs[j].classList.toggle('active', key === 'all' || secs[j].id === 'ach-' + key);
    }
    var btns = bar.querySelectorAll('button');
    for (var k = 0; k < btns.length; k++) {
      btns[k].setAttribute('aria-selected', btns[k].getAttribute('data-tab') === key ? 'true' : 'false');
    }
    if (push && history.replaceState) { history.replaceState(null, '', '#' + key); }
  }
  bar.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (b) { show(b.getAttribute('data-tab'), true); }
  });
  show(location.hash.replace('#', '') || 'all', false);
})();
</script>
