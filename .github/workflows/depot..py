            - name: Use Depot
  # You may pin to the exact commit or the version.
  # uses: depot/use-action@90146d58d088d969746f73da293453f402eeee13
  uses: depot/use-action@v1.2.0
  with:
    # Version of the Depot CLI to install. If unspecified or set to "latest",
the latest version for the target platform will be installed. Example: "0.0.2".
    version: # optional, default is latest
    # If set, will populate the `DEPOT_PROJECT_ID` environment variable.
    project: # optional, default is 
    # If set, will populate the `DEPOT_TOKEN` environment variable.
    token: # optional, default is 
    # Version of the Depot CLI to install. If unspecified or set to "latest",
the latest version for the target platform will be installed. Example: "0.0.2".
    version: # optional, default is latest
    # If set, will populate the `DEPOT_PROJECT_ID` environment variable.
    project: # optional, default is 
    # If set, will populate the `DEPOT_TOKEN` environment variable.
    token: # optional, default is 
    # If set, will install the `buildx build` shim.
    shim-buildx: # optional, default is true
          
