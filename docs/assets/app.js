(function () {
  var root = document.documentElement;
  root.classList.remove("no-js");

  function store(key, value) {
    try {
      if (value === undefined) return localStorage.getItem(key);
      localStorage.setItem(key, value);
    } catch (e) {
      return null;
    }
  }

  /* ---------- theme ---------- */
  var toggle = document.getElementById("theme-toggle");
  function currentTheme() {
    return root.getAttribute("data-theme") === "dark" ? "dark" : "light";
  }
  function paintToggle() {
    if (!toggle) return;
    var dark = currentTheme() === "dark";
    toggle.querySelector(".icon").textContent = dark ? "light_mode" : "dark_mode";
    toggle.setAttribute("aria-label", dark ? "Switch to light theme" : "Switch to dark theme");
  }
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      store("theme", next);
      paintToggle();
    });
    paintToggle();
  }

  /* ---------- app bar elevation ---------- */
  var bar = document.querySelector(".appbar");
  function onScroll() {
    if (bar) bar.classList.toggle("scrolled", window.scrollY > 8);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- ripple ---------- */
  document.addEventListener("pointerdown", function (e) {
    var el = e.target.closest(".btn, .icon-btn");
    if (!el) return;
    var r = el.getBoundingClientRect();
    var size = Math.max(r.width, r.height);
    var dot = document.createElement("span");
    dot.className = "ripple";
    dot.style.width = dot.style.height = size + "px";
    dot.style.left = e.clientX - r.left - size / 2 + "px";
    dot.style.top = e.clientY - r.top - size / 2 + "px";
    el.appendChild(dot);
    setTimeout(function () { dot.remove(); }, 650);
  });

  /* ---------- reveal on scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add("in");
          io.unobserve(en.target);
        }
      });
    }, { threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- active section in nav ---------- */
  var links = document.querySelectorAll("[data-nav]");
  var sections = [];
  links.forEach(function (a) {
    var id = a.getAttribute("data-nav");
    var sec = document.getElementById(id);
    if (sec && sections.indexOf(sec) === -1) sections.push(sec);
  });
  if (sections.length && "IntersectionObserver" in window) {
    var visible = {};
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { visible[en.target.id] = en.isIntersecting; });
      var current = null;
      sections.forEach(function (s) { if (!current && visible[s.id]) current = s.id; });
      if (!current) return;
      links.forEach(function (a) {
        a.classList.toggle("active", a.getAttribute("data-nav") === current);
      });
    }, { rootMargin: "-30% 0px -55% 0px" });
    sections.forEach(function (s) { spy.observe(s); });
  }

  /* ---------- project filter ---------- */
  var chips = document.querySelectorAll("button.chip[data-filter]");
  var cards = document.querySelectorAll(".pcard");
  var count = document.getElementById("project-count");
  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      var f = chip.getAttribute("data-filter");
      chips.forEach(function (c) { c.setAttribute("aria-pressed", c === chip ? "true" : "false"); });
      var shown = 0;
      cards.forEach(function (card) {
        var tags = (card.getAttribute("data-tags") || "").split("|");
        var ok = f === "all" || tags.indexOf(f) !== -1;
        card.hidden = !ok;
        if (ok) shown += 1;
      });
      if (count) count.textContent = shown + (shown === 1 ? " project" : " projects");
    });
  });
})();
