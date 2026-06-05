// Exibir mensagem de sucesso após redirecionamento do Formspree
if (new URLSearchParams(window.location.search).get('enviado') === '1') {
  window.scrollTo({ top: document.getElementById('contato').offsetTop - 80, behavior: 'smooth' });
  setTimeout(() => {
    const msg = document.createElement('div');
    msg.style.cssText = 'position:fixed;top:90px;left:50%;transform:translateX(-50%);background:#03111F;color:#fff;padding:16px 28px;border-radius:10px;font-size:1rem;font-weight:600;z-index:999;box-shadow:0 4px 20px rgba(0,0,0,0.3)';
    msg.textContent = '✓ Mensagem enviada! Entraremos em contato em breve.';
    document.body.appendChild(msg);
    setTimeout(() => msg.remove(), 6000);
  }, 500);
}

function toggleMenu() {
  document.querySelector('nav').classList.toggle('open');
}

async function enviarFormulario(e) {
  e.preventDefault();
  const form = e.target;
  const feedback = document.getElementById('form-feedback');
  const btn = form.querySelector('.btn-submit');

  btn.textContent = 'Enviando...';
  btn.disabled = true;
  feedback.style.color = '';
  feedback.textContent = '';

  try {
    const response = await fetch(form.action, {
      method: 'POST',
      body: new FormData(form),
      headers: { 'Accept': 'application/json' }
    });

    if (response.ok) {
      feedback.style.color = '#16a34a';
      feedback.textContent = '✓ Mensagem enviada! Entraremos em contato em breve.';
      form.reset();
    } else {
      feedback.style.color = '#dc2626';
      feedback.textContent = 'Erro ao enviar. Tente novamente ou entre em contato por telefone.';
    }
  } catch {
    feedback.style.color = '#dc2626';
    feedback.textContent = 'Erro de conexão. Verifique sua internet e tente novamente.';
  }

  btn.textContent = 'Enviar mensagem';
  btn.disabled = false;
  setTimeout(() => { feedback.textContent = ''; }, 8000);
}

function trocarVideo(el) {
  document.querySelectorAll('.video-thumb').forEach(t => t.classList.remove('active'));
  el.classList.add('active');
  const video = document.getElementById('main-video');
  const label = document.getElementById('video-label');
  video.src = el.dataset.src;
  label.textContent = el.dataset.label;
  video.play();
}

// Highlight nav link on scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('nav a[href^="#"]');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => {
    if (window.scrollY >= s.offsetTop - 80) current = s.id;
  });
  navLinks.forEach(a => {
    a.classList.remove('active');
    if (a.getAttribute('href') === '#' + current) a.classList.add('active');
  });
});
