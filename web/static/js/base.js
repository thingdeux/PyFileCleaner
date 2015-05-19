/**
 * Created by Josh on 5/18/15.
 */

$(document).ready(function() {
    function post(location) {
        $.ajax({
           type: "POST",
           url: location
        });
    }

    $("#purge-button").click(function() {
            post("/purge/logs/");
        }
    )

    $("#scan-button").click(function() {
            post("/scan");
        }
    )

    $("#delete").click(function() {
            post("/delete");
        }
    )

    $(".file-del").click(function(event) {
            var file_id = event.target.attributes.getNamedItem('fileid');
            post("/delete/file/" + file_id.value + "/");
            location.reload();
        }
    )

    $(".file-move").click(function(event) {
            var file_id = event.target.attributes.getNamedItem('fileid');
            post("/move/" + file_id.value + "/");
            location.reload();
        }
    )

    $(".folder-del").click(function(event) {
            var file_id = event.target.attributes.getNamedItem('fileid');
            post("/delete/folder/" + file_id.value + "/");
            location.reload();
        }
    )




});