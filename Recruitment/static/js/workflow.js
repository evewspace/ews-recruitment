$(document).ready(function(){ GetWorkflowList(); });

function GetWorkflowList(){
    $.ajax({
        type: "GET",
        url: "/recruitment/workflow/",
        success: function(data){
            $('#workflow_holder').html(data);
        }
    });
}

function GetAddWorkflowDialog(){
    $.ajax({
        type: "GET",
        url: "/recruitment/workflow/new/",
        success: function(data){
            recreateModalHolder();
            $('#modalHolder').html(data);
            $('#modalHolder').parent().show();
        }
    });
}

function GetEditWorkflowDialog(step_id){
    $.ajax({
        type: "GET",
        url: "/recruitment/workflow/edit/" + step_id + "/",
        success: function(data){
            recreateModalHolder();
            $('#modalHolder').html(data);
            $('#modalHolder').parent().show();
        }
    });
}

function SaveNewWorkflowAction() {
    $.ajax({
        type: "POST",
        url: "/recruitment/workflow/new/",
        data: $('#add-workflow-item-form').serialize(),
        success: function(){
            $('#modalHolder').parent().hide();
            GetWorkflowList();
        }
    });
}

function EditWorkflowAction(step_id) {
    $.ajax({
        type: "POST",
        url: "/recruitment/workflow/edit/" + step_id + "/",
        data: $('#add-workflow-item-form').serialize(),
        success: function(){
            $('#modalHolder').parent().hide();
            GetWorkflowList();
        }
    });
}

function DeleteWorkflowAction(step_id) {
	$.ajax({
        type: "POST",
        url: "/recruitment/workflow/delete/" + step_id + "/",
        success: function(){
            GetWorkflowList();
        }
    });
}
