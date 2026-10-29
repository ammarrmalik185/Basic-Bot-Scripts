var content = []
for (var i of document.getElementsByClassName("event-item")){
    var title = i.getElementsByClassName("commit")[0]?.innerText;
    if (!title) continue;
    title = title.split(" · ")[1];
    var time = i.getElementsByTagName("time")[0].title;
    var repo = i.getElementsByClassName("project-name")[0].innerText;
    var repoPath = i.getElementsByClassName("namespace-name")[0].innerText;
    
    content.push({title, time, repoPath, repo})
}