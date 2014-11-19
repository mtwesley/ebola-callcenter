
jQuery(document).ready(function() {

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