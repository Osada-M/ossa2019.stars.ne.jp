const ver = 'version 2.5 (2021-08-27)';

'use stript';

//バージョン情報読み込み
document.getElementById('version').textContent = ver;

document.getElementById('startF').onsubmit = function() {
    event.preventDefault();
    let year = document.getElementById('startF').year.value;
    let toi = document.getElementById('startF').toi.value;
    var kisetsu = document.getElementsByName('kisetsu');
    var noon = document.getElementsByName('noon');

    for (var k = '', i = kisetsu.length; i--;) {
        if (kisetsu[i].checked) {
            var k = kisetsu[i].value;
            break;
        }
    }
    for (var n = '', i = noon.length; i--;) {
        if (noon[i].checked) {
            var noon_a = noon[i].value;
            break;
        }
    }

    function func(str) {
        return str.replace(/[０-９]/g, function(s) {
            return String.fromCharCode(s.charCodeAt(0) - 0xFEE0);
        });
    }
    year = func(year);
    toi = func(toi);

    var reiwa = new Boolean(false);
    if (year.length === 1) {
        year = "0" + year;
        reiwa = true;
    }

    var noon_buf = 'q';
    var noon_buf_a = '#showAnswerBtn';
    if (noon_a === 'pm') {
        noon_buf = 'pm';
        noon_buf_a = '#splitWindowBtn';
        if (toi.length === 1) {
            toi = '0' + toi;
        }
    }

    if ((k === '' || year === '' || toi === '') || (year === '00')) {
        document.getElementById('ans').textContent = '入力が正しくない';
    } else {
        if(reiwa === true){
            document.getElementById('nendo_result').textContent = '令和 '+year+' 年';
        }else{
            document.getElementById('nendo_result').textContent = '平成 '+year+' 年';
        }
        if (k === 'haru' && year === '01') {
            document.getElementById('ans').textContent = '令和 1 年度に春試験は存在しません。';
        } else if (k === 'aki' && year === '31') {
            document.getElementById('ans').textContent = '平成 31 年度に秋試験は存在しません。';
        } else if (Number(year) >= 32) {
            document.getElementById('ans').textContent = '平成 '+year+' 年は存在しません。';
        } else if (Number(year) <= 12 && Number(year) >= (Number(new Date().getFullYear()) - 2019)) {
            document.getElementById('ans').textContent = '平成/令和 '+year+' 年度の試験は存在しないか、解答が公開されていません。';
        } else if (Number(toi) <= 0) {
            document.getElementById('ans').textContent = '問 '+toi+' は存在しません。';
        } else if (k === 'toku' && year !== '23') {
            document.getElementById('ans').textContent = '平成/令和 '+year+' 年度に特別試験は存在しません。';
        } else if (year === '23' && k === 'haru' ) {
            document.getElementById('ans').textContent = '平成 23 年度に春試験は存在しません。';
        } else if ((Number(year) >= 13 && Number(year) <= 20 ) && noon_a === 'pm') {
            document.getElementById('ans').textContent = '平成 '+year+' 年度に午後試験は存在しません。';
        } else {
            url = 'https://www.fe-siken.com/kakomon/'+year+'_'+k+'/'+noon_buf+toi+'.html';
            console.log(url);
            document.getElementById('ans').innerHTML = '<iframe src='+url+noon_buf_a+' width="650" height="400"></iframe>';
        }
    }
}
