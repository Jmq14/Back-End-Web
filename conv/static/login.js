function login(){
  history.pushState({}, 0, 'http://'+window.location.host+'/online/login/');
  document.getElementById('regist').style.display = 'none';
  document.getElementById('login').style.display = 'inline';
}
function regist(){
  history.pushState({}, 0, 'http://'+window.location.host+'/online/regist/');
  document.getElementById('login').style.display = 'none';
  document.getElementById('regist').style.display = 'inline';
}
function closeWindow(){
  history.pushState({}, 0, 'http://'+window.location.host+'/online/');
  document.getElementById('login').style.display = 'none';
  document.getElementById('regist').style.display = 'none';
}
function buttunClicked(){
  
}