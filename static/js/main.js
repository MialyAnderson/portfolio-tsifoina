// Menu mobile
const toggle = document.querySelector(".nav-toggle");
const links = document.getElementById("nav-links");

if (toggle && links) {
  toggle.addEventListener("click", () => {
    const open = links.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
  });
  links.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      links.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    })
  );
}

// Onglets des projets (clavier : flèches gauche/droite)
const tabs = Array.from(document.querySelectorAll('[role="tab"]'));

function selectTab(tab) {
  tabs.forEach((t) => {
    const selected = t === tab;
    t.setAttribute("aria-selected", String(selected));
    t.tabIndex = selected ? 0 : -1;
    document.getElementById(t.getAttribute("aria-controls")).hidden = !selected;
  });
}

tabs.forEach((tab, i) => {
  tab.addEventListener("click", () => selectTab(tab));
  tab.addEventListener("keydown", (e) => {
    let next = null;
    if (e.key === "ArrowRight") next = tabs[(i + 1) % tabs.length];
    if (e.key === "ArrowLeft") next = tabs[(i - 1 + tabs.length) % tabs.length];
    if (next) {
      e.preventDefault();
      next.focus();
      selectTab(next);
    }
  });
});

// Visionneuse d'images
const dialog = document.querySelector(".lightbox");

if (dialog) {
  const big = dialog.querySelector("img");
  document.querySelectorAll("[data-zoom]").forEach((img) => {
    img.tabIndex = 0;
    const open = () => {
      big.src = img.src;
      big.alt = img.alt;
      dialog.showModal();
    };
    img.addEventListener("click", open);
    img.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        open();
      }
    });
  });
  dialog.querySelector(".lightbox-close").addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (e) => {
    if (e.target === dialog) dialog.close();
  });
}
