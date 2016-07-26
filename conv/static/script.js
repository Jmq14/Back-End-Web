function login(){
  history.replaceState({}, 0, 'http://'+window.location.host+'/online/login/');
  document.getElementById('regist').style.display = 'none';
  document.getElementById('login').style.display = 'inline';
}
function regist(){
  history.replaceState({}, 0, 'http://'+window.location.host+'/online/regist/');
  document.getElementById('login').style.display = 'none';
  document.getElementById('regist').style.display = 'inline';
}
function closeWindow(){
  history.replaceState({}, 0, 'http://'+window.location.host+'/online/');
  document.getElementById('login').style.display = 'none';
  document.getElementById('regist').style.display = 'none';
}

$(document).ready(function(){
	$('#mymusic').click(function(){
		alert('mymusic clicked!');
	});
})

$(document).pjax('a', '#g_content');