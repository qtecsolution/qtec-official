
function change_status(id, status, sector, url) {

	var data = {'id': id, 'status': status, 'sector': sector, 'csrfmiddlewaretoken':  csrf}
	console.log(data)
	$.ajax({
		url: url,
		data: data,
		type: "POST",
		success: function (data) {
			toastr.success('Status changed successfully')
			setTimeout(function () {
				location.reload()
			}, 1200);
		},
		error: function (data) {
		}
	});
}


function fireModal(order_id){
	$("#deliverOrder").val(order_id)
	$("#agreeModal").modal('show')
}
