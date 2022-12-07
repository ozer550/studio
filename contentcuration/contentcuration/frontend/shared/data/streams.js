export class Sync {
  constructor() {
    this._transformStream = new TransformStream({
      transform(message, controller) {
        controller.enqueue(message);
      }
    });
    this._streamWriter = this._transformStream.writable.getWriter();
  }

  /**
   * @return {ReadableStream<any>}
   */
  get readableStream() {
    return this._transformStream.readable;
  }

  _writeToStream(message) {
    return this._streamWriter.write(message);
  }
}
