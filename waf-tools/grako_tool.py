# -*- coding: utf-8 -*-
"""Tool for running Grako, the grammar compiler."""

# Named 'grako_tool' so as to not collide with possible imports of the grako
# module.

import os

import waflib

EXT_IN = '.ebnf'
EXT_OUT = '.py'

def configure(ctx):
    ctx.find_program('grako')

class grako_task(waflib.Task.Task):
    """Run grako."""

    vars = ['GRAKO']
    ext_in = EXT_IN
    ext_out = EXT_OUT

    def run(self):
        input_path = self.inputs[0].abspath()
        return self.exec_command(self.env.GRAKO + [
            # The default name is the basename of the grammar file.
            # However, we like to name our files lowercase, but the class
            # name should be uppercase.
            '--name', os.path.splitext(
                os.path.basename(input_path))[0].capitalize(),
            '--output', self.outputs[0].abspath(),
            input_path,
        ])

@waflib.TaskGen.extension(EXT_IN)
def process_ebnf(task_gen, in_node):
    # Allow the user to override the default output file.
    # TODO: For now, we are forcing the 'target' attribute to be a node.
    out_node = getattr(task_gen, 'target') or in_node.change_ext(EXT_OUT)

    task_gen.create_task('grako', src=in_node, tgt=out_node)
