var P;

window.addEventListener("load", function(){
    window.cookieconsent.initialise({
        "palette": {
            "popup": {
                "background": "#237afc"
            },
            "button": {
                "background": "#fff",
                "text": "#237afc"
            }
        },
        "type": "opt-out",
        "content": {
            "href": "{% url 'registration:terms_and_conditions' %}"
        },
        revokeBtn: '<div class=""></div>'
    }, function (popup) {
            P = popup;
        });
});
