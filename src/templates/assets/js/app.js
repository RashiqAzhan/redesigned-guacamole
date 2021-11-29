window.$ = window.jQuery = require('jquery');
import 'startbootstrap-sb-admin-2/js/sb-admin-2'
import Vue from 'vue';
import App from './App.vue'
window.Vue = Vue

Vue.component('create-product', require('./components/product/CreateProduct.vue').default)
Vue.component('update-product', require('./components/product/UpdateProduct.vue').default)

const app = new Vue({
    el: '#app'
})

Vue.createApp(App).mount('#app')
