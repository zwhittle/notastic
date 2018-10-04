import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('projects');
  this.route('clients');
  this.route('notes');
  this.route('project', { path: 'projects/:project_id'});
  this.route('client', { path: 'clients/:client_id'});
  this.route('note', { path: 'note/:client_id'});
  this.route('create-project');
  this.route('create-client');
  this.route('create-note');
});

export default Router;
