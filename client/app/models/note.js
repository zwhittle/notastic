import DS from 'ember-data';

export default DS.Model.extend({
  project: DS.belongsTo('project'),
  client: DS.belongsTo('project'),
  body: DS.attr(),
  created: DS.attr(),
  owner: DS.attr()
});
