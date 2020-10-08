window.onload = function () {
    $('.shopping-cart-list').on('click', 'input[type="number"]', function () {
        var t_href = event.target;

        $.ajax({
            url: "/shopping_cartapp/edit/" + t_href.name + "/" + t_href.value + "/",

            success: function (data) {
                $('.shopping-cart-list').html(data.result);
            },
        });

        event.preventDefault();
    });
}