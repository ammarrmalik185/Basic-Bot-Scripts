let containers = document.getElementsByClassName("media-body media-vertical-align");

for (let container in containers){
    let name = containers[container].getElementsByTagName('h4')[0];
    console.log(name.innerText);
}