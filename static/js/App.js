import Vue from 'vue'
import VueResource from 'vue-resource'
import Exemplo from './components/example.vue'
import lodash from 'lodash'

Vue.use(VueResource, lodash)

new Vue(Exemplo).$mount('.exemplo')