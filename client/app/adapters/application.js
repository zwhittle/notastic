import DS from 'ember-data';
import { computed } from '@ember/object';

export default DS.JSONAPIAdapter.extend({
  host: computed(function(){
    return 'http://127.0.0.1:8000';
  }),

  namespace: 'api'
});
