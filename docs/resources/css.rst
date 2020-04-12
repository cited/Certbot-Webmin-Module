**********************
CSS
**********************

The screenshots in the documentation use a Material Design CSS Extension we created.

This can be added directly to Webmin > Configuration > Webmin Themes

In addition to making the screens a bit more vivid, it also increaes the size of objects on the page as well as padding, making it easier to work with


.. code-block:: css
   :linenos:
   
   	.row.icons-row .icons-container {
    	border-radius: 25px!important;
    	-webkit-filter: none!important;
    	filter: none!important;
	}

	html[data-theme="brown"] #sidebar {
    	background: 
	darkslategray!important;}

	.panel-default>.panel-heading {
    	color: #fff;
    	background-color: rgb(0, 188, 212)!important;text-align:left !important;
    
	}

	.panel-default>.panel-heading, .panel-default { 
	border-top-left-radius: 5px !important;
    	border-top-right-radius: 5px !important;
	}
	.panel-default , .panel{ 
	border-bottom-left-radius: 5px !important;border-top:0 !important;border-top-width: 0px;
    	border-bottom-right-radius: 5px !important;
    	box-shadow: 0 2px 2px 0 rgba(0,0,0,.14), 0 3px 1px -2px rgba(0,0,0,.12), 0 1px 5px 0 rgba(0,0,0,.2);
	}

	.row.icons-row .icons-container:not(.highlighted) {
    	border-radius: 5px !important;
    	background: rgb(255, 255, 255) !important;
    	box-shadow: 0 2px 2px 0 rgba(0,0,0,.14), 0 3px 1px -2px rgba(0,0,0,.12), 0 1px 5px 0 rgba(0,0,0,.2);
	}

	h2.form-signin-heading {
    	display: none !important;
	}

	i.wbm-webmin {
    	display: none !important;
	}

	.card {
    	font-size: .875rem;
    	font-weight: 400
	}

	.btn:not(.btn-round), button.btn:not(.btn-round), .csf-container input[type='submit']:not(.btn-round), .csf-container button.input:not(.btn-round), input[type='submit']:not(.btn-round) {
    	text-align: center;
    	vertical-align: middle;
    	font-size: 1rem;
    	line-height: 1.5;
    	border-radius: 0.325em !important;
    	transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
    	text-transform: uppercase;
    	cursor: pointer;
    	border: 0;
    	outline: 0;
    	transition: box-shadow .2s cubic-bezier(.4,0,1,1),background-color .2s cubic-bezier(.4,0,.2,1),color .2s cubic-bezier(.4,0,.2,1) !important;
    	will-change: box-shadow,transform;
    	color: rgba(0,0,0,.87);
    	background-color: rgb(255, 255, 255);
    	border-color: rgb(204, 204, 204) !important;
    	box-shadow: 0 2px 2px 0 rgba(0,0,0,.14), 0 3px 1px -2px rgba(0,0,0,.2), 0 1px 5px 0 rgba(0,0,0,.12) !important;
    	margin-left: 0 !important;
    	margin-right: 0 !important
	}

	html[data-script-name*='settings-editor_read.cgi'] #content .CodeMirror+.ui_form_end_buttons .btn {
    	margin-left: 0 !important;
    	margin-right: 0 !important
	}

	html[data-script-name*='settings-editor_read.cgi'] #content .CodeMirror+.ui_form_end_buttons td:last-child .btn {
    	margin-left: 0 !important;
    	margin-right: 5px !important
	}

	.btn-group .btn,.btn {
    	box-shadow: 0 2px 2px 0 rgba(0,0,0,.14), 0 3px 1px -2px rgba(0,0,0,.2), 0 1px 5px 0 rgba(0,0,0,.12);
	}

	.btn-group>.btn:first-child:not(:last-child):not(.dropdown-toggle) {
    	border-top-right-radius: 0 !important;
    	border-bottom-right-radius: 0 !important;
	}

	.btn-group>.btn:last-child:not(:first-child):not(.dropdown-toggle) {
    	border-top-left-radius: 0 !important;
    	border-bottom-left-radius: 0 !important;
	}

	body .btn.btn-primary {
    	color: rgb(255, 255, 255) !important;
    	background-color: rgb(63, 81, 181) !important;
    	border-color: rgb(63, 81, 181) !important;
	}
  	body .btn.btn-default {
	color: rgba(0, 0, 0, 0.87);
    	background-color: rgba(153, 153, 153, 0.2);
    	border-color: rgba(153, 153, 153, 0.2);
    	}
	body .btn.btn-success {
    	color: rgb(255, 255, 255) !important;
    	background-color: rgb(76, 175, 80) !important;
    	border-color: rgb(76, 175, 80) !important;
	}

	.btn.btn-secondary {
    	color: rgb(255, 255, 255) !important;
    	background-color: rgb(108, 117, 125) !important;
    	border-color: rgb(108, 117, 125) !important;
	}

	.btn.btn-info, .btn.btn-inverse, .btn.ui_link.btn-inverse,.btn-tiny, .ui_link.btn.btn-inverse.btn-tiny.ui_link_replaced, .btn-inverse {
    	color: rgb(255, 255, 255) !important;
    	background-color: rgb(3, 169, 244) !important;
    	border-color: rgb(3, 169, 244) !important;
	}

	.btn.btn-info:hover, .btn.btn-inverse:hover, .btn.ui_link.btn-inverse:hover,.btn-tiny:hover, .ui_link.btn.btn-inverse.btn-tiny.ui_link_replaced:hover, .btn-inverse:hover,

	.btn.btn-inverse:hover, .btn.ui_link.btn-inverse:hover, .btn-tiny:hover, .ui_link.btn.btn-inverse.btn-tiny.ui_link_replaced:hover, .btn-inverse:hover{
	border-color: rgb(255, 255, 255) !important;background-color: rgb(3, 169, 244) !important;
	}

	.btn:hover {
    	cursor: pointer !important;
	}
	.btn.btn-warning {
    	color: rgb(255, 255, 255) !important;
    	background-color: rgb(255, 87, 34) !important;
    	border-color: rgb(255, 87, 34) !important;
	}

	.btn.btn-danger {
    	color: rgb(255, 255, 255) !important;
    	background-color: rgb(244, 67, 54) !important;
    	border-color: rgb(244, 67, 54) !important;
	}

	.alert-success {
    	color: rgb(40, 91, 42);
    	background-color: rgb(219, 239, 220);
    	border-color: rgb(205, 233, 206);
	}.alert-danger {
    	color: rgb(127, 35, 28);
    	background-color: rgb(253, 217, 215);
    	border-color: rgb(252, 202, 199);
	}.alert-primary {
    	color: rgb(33, 42, 94);
    	background-color: rgb(217, 220, 240);
    	border-color: rgb(201, 206, 234);
	}.alert-secondary {
    	color: rgb(56, 61, 65);
    	background-color: rgb(226, 227, 229);
    	border-color: rgb(214, 216, 219);
	}.alert-warning {
    	color: rgb(133, 45, 18);
    	background-color: rgb(255, 221, 211);
    	border-color: rgb(255, 208, 193);
	}.alert-info {
    	color: rgb(2, 88, 127);
    	background-color: rgb(205, 238, 253);
    	border-color: rgb(184, 231, 252);
	}.alert-light {
    	color: rgb(127, 127, 127);
    	background-color: rgb(253, 253, 253);
    	border-color: rgb(252, 252, 252);
	}.alert-dark {
    	color: rgb(34, 34, 34);
    	background-color: rgb(217, 217, 217);
    	border-color: rgb(202, 202, 202);
	}
	#right-side-tabs .btn-tiny.ui_submit.ui_form_end_submit, #content #system-status .btn-tiny.ui_submit.ui_form_end_submit {
    	line-height: 21px;
    	padding: 5px 12px !important;    height: 32px !important;
	}
	.table-subtable tbody tr td, .panel-body .table-subtable tr th, .panel-body .table-subtable tr td, .table-subtable tbody tr td, .panel-body tr th, .panel-body tr td {
    	padding: .75rem !important;
	}

  	body.csf .dataTables_filter input[type='search'], body .dataTables_filter input[type='search'], .csf-container input[type='text'], .csf-container input[type='search'], .csf-container input, .csf-container select, input[id^='CSF'], input[type='button'], input[type='reset'], input[name]:not([type='image']):not([type='checkbox']):not([type='radio']):not(.btn):not(.session_login), input[name]:not([type='image']):not(.sidebar-search):not([type='button']):not([type='checkbox']):not([type='radio']):not(.btn), .csf-container input[type='text'], .csf-container input[type='search'], .chooser_button, .form-control {
    	font-size: 1rem;
    	box-sizing: content-box;
    	width: 100%;
    	height: 3rem;
    	margin: 0;
    	padding: 0;
    	-webkit-transition: box-shadow .3s,border .3s;
    	transition: box-shadow .3s,border .3s;
    	border: none;
    	border-bottom: 1px solid rgb(158, 158, 158);
    	border-radius: 0;
    	outline: 0;
    	background-color: rgba(0, 0, 0, 0);
    	box-shadow: none;font-size:16px;padding-left:5px;padding-right:5px;
	}

	input[name]:not([type='image']):not([type='checkbox']):not([type='radio']):not(.btn):not(.session_login):focus, input[name]:not([type='image']):not(.sidebar-search):not([type='button']):not([type='checkbox']):not([type='radio']):not(.btn):focus, .csf-container input[type='text']:focus, .csf-container input[type='search']:focus, .chooser_button:focus, .form-control:focus{
	border-bottom-width:2px;border-bottom-color :  rgb(63, 81, 181)
	}

	li.user-link, li.user-link span, li.user-link, li.user-link i {
    	background: rgb(85, 189, 212);
    	color: rgb(255, 255, 255) !important;
    	border-radius: 5px !important;
    	border: 0 !important;
    	line-height: 18px;
	}
	html[data-theme="brown"] #sidebar .form-group .form-control.sidebar-search::placeholder{
	color:#bbb !important
	}
	html[data-theme="brown"] #sidebar .form-group .form-control.sidebar-search{
	color: #fff!important;
	}

Above can be pasted into Theme Extensions
