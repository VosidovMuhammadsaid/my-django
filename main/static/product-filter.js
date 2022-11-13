$(document).ready(function(){
    $(".ajaxLoader").hide();
    $(".filter-checkbox").on('click',function(){
        var _filterObj={};
        $(".filter-checkbox").each(function(index,el){
            var _filterVal=$(this).val();
            var _filterKey=$(this).data('filter');
            _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(){
                return el.value;
            });
        });
        
        $.ajax({
            url:'/filter-data',
            data:_filterObj,
            dataType:'json',
            beforeSend:function(){
                $(".ajaxLoader").show();
            },
            success:function(res){
                $(".ajaxLoader").hide();
            }
        });
    });
});