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


});