const url ="http://localhost:5000/predict";
function Predict(){

    const result = document.getElementById('result');
    result.textContent="Flipping...";
    let headers = new Headers();

    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');

    headers.append('Access-Control-Allow-Origin', 'http://localhost:5000');
    headers.append('Access-Control-Allow-Credentials', 'true');


    fetch(url)
    .then((resp) => resp.json())
    .then(function(data){
        result.textContent=data.Predict;
        console.log(result.textContent)
    }).catch(function (error){
        console.log(error);
    })
}

let second_img = document.querySelector(".second-img");

let rotate2021 = () => {
  console.log('animate')
  second_img.style.animationName = "rotate2021";
  second_img.style.animationDuration = "2s";

  setTimeout(() => {
    second_img.style.animationName = "";
  }, 2000);
}