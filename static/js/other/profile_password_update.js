



// for disabling duplicate + sign
let count = 0
$("#phone").keypress(function(event) {
    var character = String.fromCharCode(event.keyCode);

    if (character == "+") {
        if (count > 0) {
            return false
        }
        if (count == 0) {
            count = 1
        }
    }
    return isValid(character);
});

function isValid(str) {
    return !/[~`!#$%\^&*()@_qwertyuiopQWERTYUIOPasdfghjklASDFGHJKLzxcvbnmZXCVBNM.=\-\[\]\\';,/{}|\\":<>\?]/g.test(str);
}