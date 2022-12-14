Fancybox.bind("#gallery a", {
    groupAll : true, // Group all items
    on : {
        ready : (fancybox) => {
            console.log(`fancybox #${fancybox.id} is ready!`);
        }}
});
