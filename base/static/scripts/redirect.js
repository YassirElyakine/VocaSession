function redirect(element,url) {
    document.getElementById(element).addEventListener('click',function(){
        window.location = '/' + url + '/';
    });
}

redirect('add_vocabulary','add');
redirect('edit_vocabulary','edit');
redirect('delete_vocabulary','delete');
redirect('logout_btn','logout');
redirect('logout_btn_mobile','logout')