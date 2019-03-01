from utils import *
import struct
import luigi
import cv2


class PreprocessImage(luigi.Task):
    filename = luigi.Parameter(default='../assets/test.png')

    def requires(self):
        return []

    def output(self):
        path = self.filename.split('/')
        return luigi.LocalTarget('{}/preproc.txt'.format('/'.join(path[:-1])))

    def run(self):
        # Get filename:
        path = self.filename.split('/')
        new_name = path[-1].split('.')
        new_name = '/'.join(path[:-1]) + '/' + \
                   ''.join(new_name[:-1]) + '_processed.' + new_name[-1]

        # Process image:
        image, gray = load_images(self.filename)
        processed_img = preprocess('morph', gray)
        cv2.imwrite(new_name, processed_img)

        with self.output().open('w') as out:
            out.write(new_name)


class ApplyOCR(luigi.Task):
    filename = luigi.Parameter(default='../assets/test_processed.png')

    def requires(self):
        return [PreprocessImage(filename=self.filename)]

    def output(self):
        path = self.filename.split('/')
        name = '.'.join(path[-1].split('.')[:-1])
        path = '/'.join(path[:-1])
        return luigi.LocalTarget('{}/{}_out.txt'.format(path, name))

    def run(self):
        with self.input()[0].open() as img_in, self.output().open('w') as out:
            self.filename = img_in.readline()
            processed_img = cv2.imread(self.filename)
            text = apply_OCR(processed_img)
            out.write(text)


if __name__ == '__main__':
    luigi.run()
