#!/usr/bin/env python3 -i

from pycocotools.coco import COCO
from file_management import ANNOTATION_FILE, get_downloaded_ids
from annotations import get_image_annotations, plot_annotations

coco = COCO(ANNOTATION_FILE)
imgs_ids = get_downloaded_ids()
anns = [get_image_annotations(coco, img_id) for img_id in imgs_ids]
