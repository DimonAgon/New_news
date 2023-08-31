
function passTime(){

    let DateTime = new Date();

    let date = {'day': DateTime.getDate(), 'month': DateTime.getMonth(), 'year': DateTime.getFullYear()};
    let time = {'hours': DateTime.getHours(), 'minutes': DateTime.getMinutes(), 'seconds': DateTime.getSeconds()};

    for (var i of [date, time]){
        for (const [key, val] of Object.entries(i)){document.getElementById(key).innerHTML = val}
    }
}

setInterval(passTime, 20);