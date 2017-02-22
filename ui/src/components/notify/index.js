import Vue from 'vue';
import Notify from './Notify';

function open(propsData) {
  const NotifyComponent = Vue.extend(Notify);
  return new NotifyComponent({
    el: document.createElement('div'),
    propsData
  });
}

export default {
  open(params) {
    const defaultParam = {};
    const propsData = Object.assign(defaultParam, params);
    return open(propsData);
  },

  info(params) {
    const defaultParam = { type: 'info' };
    const propsData = Object.assign(defaultParam, params);
    return open(propsData);
  },

  warning(params) {
    const defaultParam = { type: 'warning' };
    const propsData = Object.assign(defaultParam, params);
    return open(propsData);
  },

  success(params) {
    const defaultParam = { type: 'success' };
    const propsData = Object.assign(defaultParam, params);
    return open(propsData);
  },

  error(params) {
    const defaultParam = { type: 'danger' };
    const propsData = Object.assign(defaultParam, params);
    return open(propsData);
  }

}