// 点击登录、注册效果
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

// 点击标签时进行的一些js操作
$(document).ready(function(){
	$('#mymusic').click(function(){
		alert('mymusic clicked!');
	});
})

// pjax绑定
$(document).pjax('a', '.g-content');

// 主页轮播效果
$(window).load(function() {
        $('#slider').nivoSlider();
    });