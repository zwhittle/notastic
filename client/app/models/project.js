import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr(),
  client: DS.belongsTo('client'),
  created: DS.attr(),
  owner: DS.attr(),
  // status: DS.belongsTo('status'),
  // project_phase: DS.belongsTo('project_phase'),
  // go_live_date: DS.attr()
});
