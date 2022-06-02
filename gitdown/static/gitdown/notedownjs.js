var editor = new Editor({
    element: document.getElementById("TextArea1")
});

editor.render();
var btn_top = document.getElementById("goTop");
window.onscroll = function()
{
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20)  btn_top.style.display = "block";
    else btn_top.style.display = "none";
}

function topFunction()
{
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
function filter( val )
{
    var tmp = document.getElementsByClassName('alert');
    for(var i=0;i<tmp.length;i++)
    {
    if(tmp[i].innerText.search(val) == -1) tmp[i].style = "display:none;";  
    else tmp[i].style = "display:block;"; 
    }
    document.getElementsByClassName('btn-close')[0].click()
}