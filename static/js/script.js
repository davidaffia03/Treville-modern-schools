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

  // ---------- Reveal on scroll ----------
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  }, {threshold:0.12});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

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