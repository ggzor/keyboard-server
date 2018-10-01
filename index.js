var ip = document.getElementById('app').getAttribute('data-ip')
var port = document.getElementById('app').getAttribute('data-port')
var url = ip + ':' + port

console.log('Running at ' + url)

var app = new Vue({
  el: '#app',
  methods: {
    press: function(key) {
      console.log(key)
      axios.post('http://' + url + '/keys', { 
        'keys': key 
      })
    }
  }
})