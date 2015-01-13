(function() {
	angular.module("rateker.backend").
	service('Me', [
		'$http',
		'Urls',
		'Fetch',
		function($http, Urls, Fetch){

		this.user = null;
		var Me = this;

		this.ready = true;



		var getThoughtsRating = function() {
			url = Urls.myThoughtsRating();

			Fetch.fetch(url, '', function(data, q) {q.resolve(data);}).then(
				function(data) {
					Me.user.thoughtsRating = data.rating;
				},
				function(error) {
					console.log(error);
				}
			);

		}

		var initUser = function(user) {
			Me.user = user;
			Me.user.thoughtsRating = null;
			getThoughtsRating();

			Me.ready = user.imageUrl != null && user.places;
		}


		this.check = function() {
			console.log(this.user);
		}


		this.getUser = function() {
			return this.user;
		}

		this.sessionInit = function(username) {


			$http.get("api/user/" + username + "/profile/", {username: username})
			.success(function(data, status, header, config) {
				initUser(data);
			});
		}

		this.init = function(user) {
			initUser(user);
		}

		this.reload = function() {
			Me.sessionInit(Me.user.username);
		}

		this.destroy = function() {
			this.user = null;
		}
	}]);
})();