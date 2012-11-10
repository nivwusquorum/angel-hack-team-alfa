var appUpdateProc; //update function

$(document).ready(function() {
	heartbeat();
});

var apptime = 1;
var nextUpdate = 1000;
function heartbeat() {
	apptime += 10;
	var addr = "static/appstate.json";
	if (apptime > nextUpdate && nextUpdate > 0) {
		nextUpdate = -1;
		$.ajax({
			url : addr,
			dataType : "json",
			success: function(data) {
				appUpdateProc(data);
				nextUpdate = apptime + 20000;
			},
			error : function(jqXHR, textStatus, errorThrown) {
				appUpdateProc(undefined, errorThrown);
				nextUpdate = apptime + 50000;
			}
		});
	}
	setTimeout(heartbeat, 10);
}

function updateApplicationState(data) {
	var state = data.state;
	var questions = state.questions;
	questions.sort(function(q1,q2) { return q2.votescore - q1.votescore; });
	
}

function addQuestion(text) {
}

function voteQuestion() {
}

function updateNow() {
	nextUpdate = apptime+1;
}

function updateApplicationState(data,error) {
	var state = data.state;
	var questions = state.questions;
	
	questions.sort(function(q1,q2) { return q2.votescore - q1.votescore; });
	
	$("#right_container").html("");
	questions.forEach(function(question) {
		var temp = $(".question-template");
		var qdiv = temp.clone();
		qdiv.find(".text").html(question.text);
		qdiv.find(".votes").html(question.votescore);
		
		qdiv.attr("class", "question");
		$("#right_container").append(qdiv);
		qdiv.show();
	});
}


// Mocks

function updateApplicationStateMock(data, error) {
	$("#callNo").html("Call: "+apptime);
	if (error) {
		$("#appstate").html("ERROR! "+error);
	} else {
		$("#appstate").html(data);
	}
}

function updateApplicationStateMock2(data,error) {
	var state = data.state;
	var questions = state.questions;
	
	questions.sort(function(q1,q2) { return q2.votescore - q1.votescore; });
	
	$("#window").html("");
	var ul = $("<ul />");
	questions.forEach(function(question) {
		ul.append("<li>"+question.text+"</li>");
	});
	$("#window").append(ul);
}