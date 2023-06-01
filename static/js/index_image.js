





let main_cover1 = document.querySelector('#main_cover1');
let main_cover2 = document.querySelector('#main_cover2');
let main_cover3 = document.querySelector('#main_cover3');

let color1 = getAverageRGB(main_cover1);
let color2 = getAverageRGB(main_cover2);
let color3 = getAverageRGB(main_cover3);


main_cover1.style.background = `rgb(${color1['r']}, ${color1['g']}, ${color1['b']})`;
main_cover2.style.background = `rgb(${color2['r']}, ${color2['g']}, ${color2['b']})`;
main_cover3.style.background = `rgb(${color3['r']}, ${color3['g']}, ${color3['b']})`;


// main_cover1.style.background = `rgb(${color1[0]}, ${color1[1]}, ${color1[2]})`;
// main_cover2.style.background = `rgb(${color2[0]}, ${color2[1]}, ${color2[2]})`;
// main_cover3.style.background = `rgb(${color3[0]}, ${color3[1]}, ${color3[2]})`;


function get_average_rgb(img) {
    var context = document.createElement('canvas').getContext('2d');
    if (typeof img == 'string') {
        var src = img;
        img = new Image;
        img.setAttribute('crossOrigin', ''); 
        img.src = src;
    }
    context.imageSmoothingEnabled = true;
    context.drawImage(img, 0, 0, 1, 1);
    return context.getImageData(0, 0, 1, 1).data.slice(0,3);
}



function getAverageRGB(imgEl) {

    var blockSize = 5, // only visit every 5 pixels
        defaultRGB = {r:0,g:0,b:0}, // for non-supporting envs
        canvas = document.createElement('canvas'),
        context = canvas.getContext && canvas.getContext('2d'),
        data, width, height,
        i = -4,
        length,
        rgb = {r:0,g:0,b:0},
        count = 0;

    if (!context) {
        return defaultRGB;
    }

    height = canvas.height = imgEl.naturalHeight || imgEl.offsetHeight || imgEl.height;
    width = canvas.width = imgEl.naturalWidth || imgEl.offsetWidth || imgEl.width;

    context.drawImage(imgEl, 0, 0);

    try {
        data = context.getImageData(0, 0, width, height);
    } catch(e) {
        /* security error, img on diff domain */
        return defaultRGB;
    }

    length = data.data.length;

    while ( (i += blockSize * 4) < length ) {
        ++count;
        rgb.r += data.data[i];
        rgb.g += data.data[i+1];
        rgb.b += data.data[i+2];
    }

    // ~~ used to floor values
    rgb.r = ~~(rgb.r/count);
    rgb.g = ~~(rgb.g/count);
    rgb.b = ~~(rgb.b/count);

    return rgb;

}