(function(){
  var menuButton=document.querySelector('.menu-toggle');
  var nav=document.querySelector('.main-nav');
  if(menuButton&&nav){
    menuButton.addEventListener('click',function(){
      var open=menuButton.getAttribute('aria-expanded')!=='true';
      menuButton.setAttribute('aria-expanded',String(open));
      nav.classList.toggle('nav-open',open);
    });
  }
  var menuItem=document.querySelector('.has-menu');
  var trigger=document.querySelector('.nav-trigger');
  if(menuItem&&trigger){
    trigger.addEventListener('click',function(){
      var open=trigger.getAttribute('aria-expanded')!=='true';
      trigger.setAttribute('aria-expanded',String(open));
      menuItem.classList.toggle('menu-open',open);
    });
    document.addEventListener('click',function(event){
      if(!menuItem.contains(event.target)){
        menuItem.classList.remove('menu-open');
        trigger.setAttribute('aria-expanded','false');
      }
    });
    document.addEventListener('keydown',function(event){
      if(event.key==='Escape'){
        menuItem.classList.remove('menu-open');
        trigger.setAttribute('aria-expanded','false');
        trigger.focus();
      }
    });
  }
  document.querySelectorAll('.main-nav a[href^="#"]').forEach(function(link){
    link.addEventListener('click',function(){
      if(nav){nav.classList.remove('nav-open');}
      if(menuButton){menuButton.setAttribute('aria-expanded','false');}
    });
  });
  var year=document.querySelector('[data-year]');
  if(year){year.textContent=new Date().getFullYear();}
})();