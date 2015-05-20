
jQuery(document).ready(function() {

    $('[data-countdown]').each(function() {
        var $this = $(this), startDate = $(this).data('countdown');
        $this.countdown({
            since: new Date(startDate),
            format: 'MS',
            layout: '{mnn}:{snn}'
        });
    });

    $('#agent_form').on("keyup keypress", function(e) {
        if ((e.keyCode || e.which) == 13) {
            e.preventDefault()
            $("#agent_action").val('submit')
            $("#agent_form").submit()
        }
    });

    $(".btn_submit").on("click", function(e) {
        $("#agent_action").val('submit')
    })

    $(".btn_skip").on("click", function(e) {
        $("#agent_action").val('skip')
    })

    $(".btn_cancel").on("click", function(e) {
        $("#agent_action").val('cancel')
    })

    $(".btn_submit, .btn_skip, .btn_cancel").on("click", function(e) {
        e.preventDefault()
        $(this).parents('form').submit()
    })
});