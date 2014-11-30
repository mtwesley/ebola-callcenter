
jQuery(document).ready(function() {

    $('#agent_form').on("keyup keypress", function(e) {
        if ((e.keyCode || e.which) == 13) {
            e.preventDefault()
            $("#agent_action").val('submit')
            $("#agent_form").submit()
        }
    });

    $(".btn_submit").on("click", function(e) {
        e.preventDefault()
        $("#agent_action").val('submit')
        $("#agent_form").submit()
    })

    $(".btn_skip").on("click", function(e) {
        e.preventDefault()
        $("#agent_action").val('skip')
        $("#agent_form").submit()
    })

    $(".btn_cancel").on("click", function(e) {
        e.preventDefault()
        $("#agent_action").val('cancel')
        $("#agent_form").submit()
    })

});