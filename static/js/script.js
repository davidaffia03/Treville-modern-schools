(function(){
  // ---------- Intro swoosh splash ----------
  const splash = document.getElementById('introSplash');
  if(splash){
    if(sessionStorage.getItem('trevilleIntroPlayed')){
      splash.remove();
    } else {
      document.body.classList.add('intro-active');
      sessionStorage.setItem('trevilleIntroPlayed', '1');
      setTimeout(()=>{
        splash.classList.add('hide');
        document.body.classList.remove('intro-active');
        setTimeout(()=> splash.remove(), 700);
      }, 4200);
    }
  }

  // ---------- Header scroll ----------
  const header = document.getElementById('siteHeader');
  window.addEventListener('scroll', ()=>{
    header.classList.toggle('scrolled', window.scrollY > 40);
  });

  // ---------- Footer year ----------
  const yr = document.getElementById('yr');
  if(yr) yr.textContent = new Date().getFullYear();

  // ---------- Hamburger menu overlay ----------
  const menuToggle = document.getElementById('menuToggle');
  const navOverlay = document.getElementById('navOverlay');

  function openMenu(){
    navOverlay.classList.add('open');
    menuToggle.classList.add('open');
    menuToggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }
  function closeMenu(){
    navOverlay.classList.remove('open');
    menuToggle.classList.remove('open');
    menuToggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  if(menuToggle && navOverlay){
    menuToggle.addEventListener('click', (e)=>{
      e.stopPropagation();
      navOverlay.classList.contains('open') ? closeMenu() : openMenu();
    });
    navOverlay.querySelectorAll('[data-close]').forEach(link=>{
      link.addEventListener('click', closeMenu);
    });
    document.addEventListener('keydown', (e)=>{
      if(e.key === 'Escape') closeMenu();
    });
    document.addEventListener('click', (e)=>{
      if(navOverlay.classList.contains('open') &&
         !navOverlay.contains(e.target) &&
         !menuToggle.contains(e.target)){
        closeMenu();
      }
    });
  }

  // ---------- Button tap ripple ----------
  document.querySelectorAll('.btn').forEach(btn=>{
    btn.addEventListener('click', function(e){
      const circle = document.createElement('span');
      const rect = this.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      circle.style.width = circle.style.height = size + 'px';
      circle.style.left = (e.clientX - rect.left - size / 2) + 'px';
      circle.style.top = (e.clientY - rect.top - size / 2) + 'px';
      circle.className = 'ripple';
      this.appendChild(circle);
      setTimeout(()=> circle.remove(), 600);
    });
  });
})();

// ---------- Scroll progress bar ----------
const progressBar = document.createElement('div');
progressBar.id = 'scrollProgress';
document.body.appendChild(progressBar);

window.addEventListener('scroll', () => {
  const scrollTop = window.scrollY;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const scrolled = (scrollTop / docHeight) * 100;
  progressBar.style.width = scrolled + '%';
});

// ---------- Reveal sections/cards on scroll, staggered ----------
const revealEls = document.querySelectorAll('.reveal, .box-reveal');

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.target.classList.contains('box-reveal')) {
      entry.target.style.transitionDelay = '0s';
    } else {
      const siblings = entry.target.parentElement.querySelectorAll('.reveal');
      const index = Array.from(siblings).indexOf(entry.target);
      const delay = 0.25 + Math.min(index, 6) * 0.08;
      entry.target.style.transitionDelay = delay + 's';
    }

    if (entry.isIntersecting) {
      entry.target.classList.add('in');
    } else {
      entry.target.classList.remove('in');
    }
  });
}, {
  threshold: 0.15,
  rootMargin: '0px 0px -60px 0px'
});

revealEls.forEach(el => revealObserver.observe(el));

// ---------- Hover-preview scroll for same-page nav links ----------
(function(){
  const overlayLinks = document.querySelectorAll('#navOverlay .overlay-links a[href*="#"]:not([href*="about-owner"])');
  let savedScrollY = null;
  let previewTimeout = null;

  overlayLinks.forEach(link => {
    const hrefParts = link.getAttribute('href').split('#');
    const targetId = hrefParts[1];
    if (!targetId) return;

    link.addEventListener('mouseenter', () => {
      const targetEl = document.getElementById(targetId);
      if (!targetEl) return;

      if (savedScrollY === null) {
        savedScrollY = window.scrollY;
      }

      clearTimeout(previewTimeout);
      previewTimeout = setTimeout(() => {
        targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 180);
    });

    link.addEventListener('mouseleave', () => {
      clearTimeout(previewTimeout);
      if (savedScrollY !== null) {
        previewTimeout = setTimeout(() => {
          window.scrollTo({ top: savedScrollY, behavior: 'smooth' });
          savedScrollY = null;
        }, 180);
      }
    });

    link.addEventListener('click', () => {
      savedScrollY = null;
      clearTimeout(previewTimeout);
    });
  });

  const ownerLink = document.querySelector('#navOverlay .overlay-links a[href*="about-owner"]');
  if (ownerLink) {
    ownerLink.addEventListener('mouseenter', () => {
      clearTimeout(previewTimeout);
    });
  }
})();