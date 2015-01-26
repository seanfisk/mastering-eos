# -*- coding: utf-8 -*-

"""Waf tool for running Fabric tasks."""

# Named 'fabric_tool' so as to not collide with possible imports of the fabric
# module.

import sys

import six
import waflib

def configure(ctx):
    ctx.find_program('fab')

@waflib.TaskGen.feature('fabric')
@waflib.TaskGen.before_method('process_source')
def apply_fabric(task_gen):
    """Set up the task generator with a Fabric task.

    This method overrides the processing by
    :py:meth:`waflib.TaskGen.process_source`.
    """
    # Initialize keywords.
    try:
        commands = getattr(task_gen, 'commands')
    except AttributeError:
        raise waflib.Errors.WafError(
            'Fabric task generator missing necessary keyword: commands')

    fabfile = getattr(task_gen, 'fabfile', 'fabfile.py')
    fabfile_node = _node_or_bust(fabfile, task_gen.path.find_resource)
    if not fabfile_node:
        raise waflib.Errors.WafError('Fabfile not found: {0}'.format(fabfile))

    # source and target aren't directly used, but they *are* passed to the
    # task, so they will be viewed as dependencies.
    #
    # Include the fabfile as a dependency so the task runs when the fabfile is
    # changed.
    in_nodes = [fabfile_node] + task_gen.to_nodes(
        getattr(task_gen, 'source', []))
    out_nodes = [_node_or_bust(t, task_gen.path.find_or_declare)
                 for t
                 in waflib.Utils.to_list(getattr(task_gen, 'target', []))]

    # Derive a new task class with the specified name if that was requested.
    try:
        name = task_gen.name
    except AttributeError:
        name = 'Fabric'
    else:
        type(name, (fabric_task,), {})

    task = task_gen.create_task(name, src=in_nodes, tgt=out_nodes)
    # Assign attributes necessary for task methods.
    task.fabfile_node = fabfile_node
    task.options = getattr(task_gen, 'options', [])
    task.commands = commands
    task.always = getattr(task_gen, 'always', False)

    # Set the task order if that was requested.
    for attr in ['after', 'before']:
        # Append an underscore to the expected keyword so that Waf doesn't dump
        # warnings in verbose mode.
        setattr(task, attr, getattr(task_gen, attr + '_', []))

    # Prevent execution of process_source. We don't need it because we are
    # handling the sources.
    # Following the lead of code in waflib:
    task_gen.source = []
    # Also possible.
    # task_gen.meths.remove('process_source')

def _escape(value):
    # Fabric uses the syntax 'command:key1=val,key2=val' syntax to pass in
    # arguments, so some escaping is necessary :\
    return value.replace('=', r'\=').replace(',', r'\,')

class fabric_task(waflib.Task.Task):
    """Task to run a Fabric command"""
    # pylint: disable=no-member

    vars = ['FAB']

    def run(self):
        return self.exec_command(
            self.env.FAB + [
                '--fabfile',
                self.fabfile_node.abspath(),
            ] + self.options + [
                '{0}:{1}'.format(
                    command,
                    ','.join(
                        '{0}={1}'.format(_escape(key), _escape(val))
                        for key, val in six.iteritems(args)))
                for command, args in six.iteritems(self.commands)
            ],
            # Don't capture the standard streams in case we get prompts.
            stdout=sys.stdout,
            stderr=sys.stderr,
        )

    def runnable_status(self):
        # Allow overriding 'always' per-instance.
        ret = super(fabric_task, self).runnable_status()
        if self.always and ret == waflib.Task.SKIP_ME:
            ret = waflib.Task.RUN_ME
        return ret

def _node_or_bust(node_or_path, node_func):
    return (node_or_path
            if isinstance(node_or_path, waflib.Node.Node)
            else node_func(node_or_path))
