"""An easy way to define and build Packer images."""
import os
from packer_builder.args import get_args
from packer_builder.build import Build
from packer_builder.distros import Distros
from packer_builder.generate_templates import GenerateTemplates


def main():
    """Packer builder main execution."""
    args = get_args()
    distros = Distros(args).get_distros()

    # Ensure output dir exists if defined
    if args.outputdir is not None:
        if not os.path.isdir:
            os.makedirs(args.outputdir)

    if args.action == 'build':
        Build(args, distros)
    elif args.action == 'list-distros':
        Distros(args).list_distros()
    elif args.action == 'generate-templates':
        GenerateTemplates(args, distros)


if __name__ == '__main__':
    main()
