[...Array(100000)].map((v, i) => i).map((i) => window.clearInterval(i));
clearInterval(TimerID);
openClassTime = Number(openClassTime) - 400000;
Duration = 400;
window.onbeforeunload = null;

const _url = "/public/PROGRESS_OUTLOG_DOING.asp";
const _data = {
    classkey: content.getCookie("cr%5Fclasskey"),
    classcount: content.getCookie("cr%5Fclasscount"),
    studykey: content.getCookie("cr%5Fstudykey"),
    contentskey: content.getCookie("cr%5Fcontentskey"),
    part: content.pageURL.slice(-10, -8) + content.pageURL.slice(-7, -5) + "01",
    page: "0" + content.pageURL.slice(-7, -5),
    duration: 400,
    Dplatform: "",
};
const request = $.ajax({
    url: _url,
    data: _data,
    method: "GET",
});

console.log(_data);
setTimeout(100);

content.progressControll = 1;
content._doNext();
