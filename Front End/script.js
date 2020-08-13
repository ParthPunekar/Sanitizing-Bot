$(document).ready(function(){
	let speed = 0;
	$('#pump1').on('click', function(e) {
		let status;
		if ($('#pump1Status').text() == 'ON') {
			$('#pump1Status').text('OFF')
			status = 'Pump1_OFF';
		} else {
			$('#pump1Status').text('ON')
			status = 'Pump1_ON';
		}

		$.ajax({
			url: "/main?status="+ status,
			method: 'GET',
			success: function(result) {
				console.log(result);
			}
		});
		e.preventDefault();
	});

	$('#pump2').on('click', function(e) {
		let status;
		if ($('#pump2Status').text() == 'ON') {
			$('#pump2Status').text('OFF')
			status = 'Pump2_OFF';
		} else {
			$('#pump2Status').text('ON')
			status = 'Pump2_ON';
		}

		$.ajax({
			url: '/main?status=' + status,
			method: 'GET',
			success: function(result) {
				console.log(result);
			}
		});
		e.preventDefault();
	});

	$('#frontLED').on('click', function(e){
		let status;
		if ($('#fLEDStatus').text() == 'ON') {
			$('#fLEDStatus').text('OFF')
			status = 'FLED_OFF';
		} else {
			$('#fLEDStatus').text('ON')
			status = 'FLED_ON';
		}

		$.ajax({
			url: '/main?status=' + status,
			method: 'GET',
			success: function(result) {
				console.log(result);
			}
		});
		e.preventDefault();
	});

	$('#rearLED').on('click', function(e) {
		let status;
		if ($('#rLEDStatus').text() == 'ON') {
			$('#rLEDStatus').text('OFF')
			status = 'RLED_OFF';
		} else {
			$('#rLEDStatus').text('ON')
			status = 'RLED_ON';
		}

		$.ajax({
			url: '/main?status=' + status,
			method: 'GET',
			success: function(result) {
				console.log(result);
			}
		});
		e.preventDefault();
	});

	$('#front').on('click', function(e) {
		$('#motion').text('FRONT');

		$.ajax({
			url: '/main?status=front',
			method: 'GET',
			success: function(result) {
				console.log(result);
			}
		});
		e.preventDefault();
	});

	$('#right').on('click', function(e) {
		$('#motion').text('RGIHT');

		$.ajax({
			url: '/main?status=right',
			method: 'GET',
			success: function (result) {
				console.log(result);
			}
		});
		e.preventDefault();
	});

	$('#left').on('click', function(e) {
		$('#motion').text('LEFT');

		$.ajax({
			url: '/main?status=left',
			method: 'GET',
			success: function(result) {
				console.log(result);
			}
		});
		e.preventDefault();
	});

	$('#stop').on('click', function(e) {
		$('#motion').text('STOP');
		$('#controls').fadeToggle();

		$.ajax({
			url: '/main?status=stop',
			method: 'GET',
			success: function(result) {
				console.log(result);
			}
		});
		e.preventDefault();
	});

	$('#back').on('click', function(e) {
		$('#motion').text('BACK');

		$.ajax({
			url: '/main?status=back',
			method: 'GET',
			success: function (result) {
				console.log(result);
			} 
		});
		e.preventDefault();
	});

	$('#speedControl').on('input', function(e) {
		$('#speedValue').text(this.value + '%');
		
		$ajax({
			url: '/main?speed=' + this.value,
			method: 'GET',
			success: function (result) {
				console.log(result);
			}
		});
		e.preventDefault();
	});

	$('#camLeft').on('click', function(e) {
		$ajax({
			url: '/main?status=cam_left',
			method: 'GET',
			success: function (result) {
				console.log(result);
			}
		});
		e.preventDefault();
	});

	$('#camRight').on('click', function(e) {
		$ajax({
			url: '/main?status=cam_right',
			method: 'GET',
			success: function (result) {
				console.log(result);
			}
		});
		e.preventDefault();
	});
});
